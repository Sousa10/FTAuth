from sre_parse import State
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import CashInAcctM, PersonM, FinStatements, StatementSections, SectionLines, LineAccounts 
from .forms import CashInAcctMForm, FinStatementsForm, StatementSectionsForm, SectionLinesForm, LineAccountsForm, SectionSelectForm, StatementSelectForm
from django.core.paginator import Paginator
from datetime import datetime
import os
from LoginRegister.utils import increment_click_count
from django.http import HttpResponseServerError
import logging
from django.urls import reverse
from django.db.models import Sum

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'transactions/main_landing_page.html', {})

def main_landing_page(request):
    click_count = increment_click_count('transactions')
    return render(request, 'transactions/main_landing_page.html', {'click_count': click_count,})

def income_accts(request):
    cashinacctms = CashInAcctM.objects.all()
    if request.method == 'POST':
        form = CashInAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transactions:income_accts')
    else:
        form = CashInAcctMForm()
    return render(request, 'transactions/FTRevenueAccts.html', {
        'form': form,
        'cashinacctms': cashinacctms,
        'title': 'Add Cash In Account',
    })


def cashinacctm_delete(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    cashinacctm.delete()

    return redirect('transactions:income_accts')

def cashinacctm_update(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    if request.method == 'POST':
        form = CashInAcctMForm(request.POST, instance=cashinacctm)
        if form.is_valid():
            form.save()
            return redirect('transactions:income_accts')
    else:
        form = CashInAcctMForm(instance=cashinacctm)
    return render(request, 'transactions/FTRevenueAccts.html', {
        'form': form,
        'cashinacctm': cashinacctm,
        'title': 'Edit Cash In Account',
    })

def populate_from_csv(csv_file):
    file_data = csv_file.read().decode("utf-8")
    csv_data = file_data.split("\n")
    for row in csv_data:
        # Skip empty rows
        if not row.strip():
            continue
        fields = row.split(",")
        # print(len(fields))
        if len(fields) < 7:  # Adjust this number based on the minimum columns you expect
            continue

        formatted_date = None
        # If TransDescription is present, create a new TransHeader record.
        if fields[0] == 'TB' and fields[2] and fields[4]:
            if fields[4]:
                try:
                    formatted_date = format_date(fields[4])
                    trans_batch = TransBatch.objects.create(
                        TransBatchName=fields[2], TransBatchDate=formatted_date or None)
                except ValueError:
                    # Handle or log the malformed date value here
                    print(f"Invalid date format for entry: {fields[4]}")

        elif fields[0] == 'TH' and fields[3] and fields[5] and fields[7]:
            if fields[5]:
                try:
                    formatted_date = format_date(fields[5])
                    current_header = TransHeader.objects.create(
                        TransBatchID=trans_batch,
                        TransDescription=fields[3],
                        TransDate=formatted_date,
                        TransNote=fields[7]
                    )
                except ValueError:
                    # Handle or log the malformed date value here
                    print(f"Invalid date format for entry: {fields[5]}")

        elif fields[0] == 'TD' and fields[2]:
            try:
                amount = int(fields[2])
                TransDetail.objects.create(
                    TransHeaderID=current_header,
                    Amount=amount,
                    DrAccount=fields[4],
                    CrAccount=fields[6]
                )
            except ValueError:
                print(f"Invalid amount format for entry: {fields[2]}")

def FTTransactions(request, batch_id=None):
    if batch_id:
        transBatch = TransBatch.objects.get(id=batch_id)
        transHeaders = transBatch.transheader_set.all()
        for transHeader in transHeaders:
            transDetail = transHeader.transdetail_set.all()
            paginator = Paginator(transDetail, 2)  # Show 10 StatementLinesLine objects per page
            page_number = request.GET.get('page', 1)  # get page number for each StatementSections instance
            page = paginator.get_page(page_number)
    else:
      transDetail = None
      page = None
    
    transBatch = TransBatch.objects.first()
    form = TemplateActionForm()
    transbatchForm = TransBatchSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'uploadDownload':
            form = TemplateActionForm(request.POST, request.FILES)
            if form.is_valid():
                if form.cleaned_data['action'] == 'download':
                    # Use the pre-existing Excel file for download
                    filename = os.path.join(os.path.dirname(
                        os.path.dirname(__file__)), "resources", "template.xlsx")
                    with open(filename, "rb") as excel:
                        response = HttpResponse(
                            excel.read(), content_type='application/vnd.ms-excel')
                        response['Content-Disposition'] = 'inline; filename=' + \
                            os.path.basename(filename)
                    return response

                elif form.cleaned_data['action'] == 'upload':
                    csv_file = request.FILES['excel_file']
                    if not csv_file.name.endswith('.csv'):
                        print("whatt!!!!")
                        messages.warning(
                            request, 'The wrong file type was uploaded')
                        return HttpResponseRedirect(request.path_info)
                    populate_from_csv(csv_file)
                    # Redirect back to the same view
                    return redirect('LoginRegister:FTTransactions', batch_id = transBatch.id)
        elif form_type == 'SelectedBatchForm':
            transbatchForm = TransBatchSelectForm(request.POST)
            if transbatchForm.is_valid():
                batchname = transbatchForm.cleaned_data['BatchName']
                transbatch = TransBatch.objects.get(TransBatchName=batchname)
                print(transbatch.id)
                transHeaders = transBatch.transheader_set.all()
                for transHeader in transHeaders:
                    transDetail = transHeader.transdetail_set.all()
                    paginator = Paginator(transDetail, 2)  # Show 10 StatementLinesLine objects per page
                    page_number = request.GET.get('page', 1)  # get page number for each StatementSections instance
                    page = paginator.get_page(page_number)
                    return redirect('LoginRegister:FTTransactions', batch_id = transbatch.id)

    else:
        form = TemplateActionForm()
        transbatchForm = TransBatchSelectForm()

    transactions = TransDetail.objects.all()
    # Assuming you want to display all the batches, headers, and details on the same page
    batch = TransBatch.objects.all()
    paginator = Paginator(transactions, 11)  # Show 11 accounts per page.
    page_number = request.GET.get("page")
    transactions_paginated = paginator.get_page(page_number)
    context = {
        'form': form,
        'transactions': transactions_paginated,
        # 'batch': batch,
        'transBatch': transBatch,
        'transbatchForm': transbatchForm,
        'transdetail': page
    }
    return render(request, 'LoginRegister/FTTransactions.html', context)


def transaction_delete(request, pk):
    transaction = get_object_or_404(TransDetail, pk=pk)
    transaction.delete()

    return redirect('LoginRegister:FTTransactions')

def show_construction(request):
    return render(request, 'transactions/show_construction.html', {})

def accounts(request):
    accounts_list = CashInAcctM.objects.all()

    # Set up Pagination
    p = Paginator(accounts_list, 15)
    page = request.GET.get('page')
    accounts_p = p.get_page(page)
    nums = "x" * accounts_p.paginator.num_pages
    return render(request, 'transactions/accounts.html', {
        'accounts_list': accounts_list,
        'accounts_p':accounts_p,
        'nums':nums
        })

def show_account(request, account_id):
    account_info = CashInAcctM.objects.get(pk=account_id)
    return render(request, 'transactions/show_account.html', {'account': account_info})

def search_accounts(request):
    if request.method == "POST":
        searched = request.POST['searched'] 
        accounts = CashInAcctM.objects.filter(Description__contains=searched)
        return render(request, 'transactions/search_accounts.html', {'searched':searched, 'accounts':accounts})
    else:
        return render(request, 'transactions/search_accounts.html', {})

def format_date(field):
    return datetime.strptime(field, '%d/%m/%y').strftime('%Y-%m-%d')

############################################
#<<<<<<<<<< Financial Statements >>>>>>>>>>#
############################################
#------------------------------------------#
       # FinStatementsV 
#------------------------------------------#
def FinStatementsV(request):
    finstmts = FinStatements.objects.all()

statementForm = FinStatementsForm()

############################################
#<<<<<<< Statement Sections >>>>>>>>>>>>>>>#
############################################
#------------------------------------------#
       # StatementSectionsV 
#------------------------------------------#
def StatementSectionsV(request, pk=None):
    # first_statement = StatementSections.objects.first()
    statement = None
    statementSections = None
    # first_section = StatementSections.objects.first()
    # section = None
    # lines = None
    page = None

    if pk is not None:
        statement = get_object_or_404(FinStatements, id=pk)
        statementSections = StatementSections.objects.filter(FinStatementsFK=statement)
        # Show 10 ListDetailsT objects per page
        paginator = Paginator(statementSections, 8)
        # get page number for each ListHeaderT instance
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        selected_statement = statement
    else:
        selected_statement = None

    statementForm = FinStatementsForm()
    statementLinesForm = SectionLinesForm()
    statementAccountForm = LineAccountsForm()
    if selected_statement:
        statementSectionsForm = StatementSectionsForm(statement=selected_statement)
    else:
        statementSectionsForm = StatementSectionsForm()
    #selectedSectionForm = SectionSelectForm()
    selectedStatementForm = StatementSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        # remember to refactor this to reduce or eliminate the ifs
        if form_type == 'StatementForm':
            print("inside statement form")
            statementForm = FinStatementsForm(request.POST)
            if statementForm.is_valid():
                saved_statement =statementForm.save()

                return redirect('transactions:statement_section_with_id', pk=saved_statement.id)
            
        elif form_type == 'StatementSectionForm':
            sectionForm = StatementSectionsForm(request.POST)
            if sectionForm.is_valid():
                saved_section =sectionForm.save()
                related_statement = saved_section.FinStatementsFK

                return redirect('transactions:statement_section_with_id', pk=related_statement.id)

        elif form_type == 'StatementLinesForm':
            print("inside lines form")
            statementLinesForm = SectionLinesForm(request.POST)
            if statementLinesForm.is_valid():
                savedLine = statementLinesForm.save()
                related_section = savedLine.SLStatementSectionsFK
                related_statement = related_section.FinStatementsFK

                return redirect('transactions:statement_section_with_id', pk=related_statement.id)
            
        elif form_type == 'StatementAccountForm':
            statementAccountForm = LineAccountsForm(request.POST)
            if statementAccountForm.is_valid():
                savedAccount = statementAccountForm.save()
                related_line = savedAccount.LAStatementLineFK
                related_section = related_line.SLStatementSectionsFK
                related_statement = related_section.FinStatementsFK

                return redirect('transactions:statement_section_with_id', pk=related_statement.id)

        elif form_type == 'SelectedStatementForm':
            selectedStatementForm = StatementSelectForm(request.POST)
            if selectedStatementForm.is_valid():
                statementName = selectedStatementForm.cleaned_data['FSName']
                statement = FinStatements.objects.get(FSName=statementName)
                statementSections = statement.statementsections_set.prefetch_related(
                    'statementsectionlines_set',
                    'statementsectionlines_set__statementlineaccounts_set'
                ).all()

                 # Calculate totals for each section
                for section in statementSections:
                    section.total = sum(line.statementlineaccounts_set.aggregate(Sum('LAAccount')).get('LAAccount__sum', 0) for line in section.statementsectionlines_set.all())
                    print(section.total)
                #Show 10 ListDetailsT objects per page
                paginator = Paginator(statementSections, 5)
                #get page number for each ListHeaderT instance
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)

                return redirect('transactions:statement_section_with_id', pk=statement.id)
    # else:
        # statementForm = FinStatementsForm()
        # statementSectionsForm = StatementSectionsForm(statement=selected_statement)
    return render(request, 'transactions/statement_lines.html', {
        'statementForm': statementForm,
        # 'first_statement': first_statement,
        'statementSectionsForm': statementSectionsForm,
        'selectedStatementForm': selectedStatementForm,
        'statementLinesForm': statementLinesForm,
        'statementAccountForm': statementAccountForm,
        'statement': statement,
        'statementSections': page,
        'title': 'Statement Sections, Lines and Accounts',
    })

#------------------------------------------#
        # StatmentDelete
#------------------------------------------#
def Statement_deleteV(request, pk):
    first_statement = FinStatements.objects.first()
    statement = get_object_or_404(FinStatements, pk=pk)
    statement.delete()

    if first_statement:
        return redirect('transactions:statement_section_with_id', pk=first_statement.id)
    else:
        return redirect('transactions:statement_section')

#------------------------------------------#
    # Statement_updateV
#------------------------------------------#
def statement_update(request, pk):
    first_statement = FinStatements.objects.first()
    statement = get_object_or_404(FinStatements, pk=pk)
    if request.method == 'POST':
        form = FinStatementsForm(request.POST, instance=statement)

        if form.is_valid():
            form.save()
            fallback_url = reverse('transactions:statement_section_with_id', kwargs={'pk':first_statement.id})
            return redirect(request.META.get('HTTP_REFERER', fallback_url))
    else:
        form = FinStatementsForm(instance=statement)

#------------------------------------------#
    # StatementSections_updateV
#------------------------------------------#
def StatementSections_updateV(request, pk):
    first_statement = FinStatements.objects.first()
    ssection = get_object_or_404(StatementSections, pk=pk)
    if request.method == 'POST':
        form = StatementSectionsForm(request.POST, instance=ssection)

        if form.is_valid():
            print("form is valid")
            form.save()
            fallback_url = reverse('transactions:statement_section_with_id', kwargs={'pk':first_statement.id})
            return redirect(request.META.get('HTTP_REFERER', fallback_url))
        else:
            print("form is not valid")
            print(form.errors)

#------------------------------------------#
        # StatmentSectionsDelete
#------------------------------------------#
def StatementSections_deleteV(request, pk):
    first_statement = FinStatements.objects.first()
    ssection = get_object_or_404(StatementSections, pk=pk)
    ssection.delete()

    if first_statement:
        return redirect('transactions:statement_section_with_id', pk=first_statement.id)
    else:
        return redirect('transactions:statement_section')

############################################
#<<<<<<<<<<<< Section Lines >>>>>>>>>>>>>>>#
############################################
#------------------------------------------#
           # SectionLinesV
#------------------------------------------#
def SectionLinesV(request):
    sllines = SectionLines.objects.all()

    if request.method == 'POST':
        form = SectionLines(request.post)

        if form.is_valid():
                form.save()
                return redirect('transactions:statement_lines')

    else:

        form = SectionLinesForm()

    return render(request, 'transactions:statement_lines.html', {
        'form': form,
        'sllines': sllines,
        'title': 'Statement Lines',
    })

#------------------------------------------#
        # StatementLinesLineUpdate
#------------------------------------------#
def SectionLines_updateV(request, pk):
    first_statement = FinStatements.objects.first()
    slline = get_object_or_404(SectionLines, pk=pk)
    if request.method == 'POST':
        form = SectionLinesForm(request.POST, instance=slline)
        if form.is_valid():
            form.save()
            fallback_url = reverse('transactions:statement_section_with_id', kwargs={'pk':first_statement.id})
            return redirect(request.META.get('HTTP_REFERER', fallback_url))
    else:
        form = SectionLinesForm(instance=slline)
    return render(request, 'transactions:statement_lines.html', {
        'form': form,
        'sllines': slline,
        'title': 'Statement Lines',
    })

#------------------------------------------#
        # StatementLinesLineDelete
#------------------------------------------#
def SectionLines_deleteV(request, pk):
    first_statement = FinStatements.objects.first()
    line = get_object_or_404(SectionLines, pk=pk)
    line.delete()

    if first_statement:
        return redirect('transactions:statement_section_with_id', pk=first_statement.id)
    else:
        return redirect('transactions:statement_section')

############################################
#<<<<<<<<<<<<<< Line Accounts >>>>>>>>>>>>>#
############################################
#------------------------------------------#
#               LineAccountsV           
#------------------------------------------#
def LineAccountsV(request):
    slaccounts = SectionLines.objects.all()
    if request.method == 'POST':
        form = LineAccountsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transactions:accounts')
    else:
        form = LineAccountsForm()
    return render(request, 'transactions/accounts.html', {
        'form': form,
        'slaccounts': slaccounts,
        'title': 'Add Account',
    })

#------------------------------------------#
#           LineAccounts_updateV           
#------------------------------------------#
def LineAccounts_updateV(request, pk):
    first_statement = FinStatements.objects.first()
    slaccount = get_object_or_404(LineAccounts, pk=pk)
    if request.method == 'POST':
        form = LineAccountsForm(request.POST, instance=slaccount)
        if form.is_valid():
            form.save()
            fallback_url = reverse('transactions:statement_section_with_id', kwargs={'pk':first_statement.id})
            return redirect(request.META.get('HTTP_REFERER', fallback_url))
    else:
        form = LineAccountsForm(instance=slaccount)
        
    return render(request, 'transactions:statement_lines.html', {})

#------------------------------------------#
#           LineAccounts_deleteV           
#------------------------------------------#
def LineAccounts_deleteV(request, pk):
    first_statement = FinStatements.objects.first()
    slaccounts = get_object_or_404(LineAccounts, pk=pk)
    slaccounts.delete()

    if first_statement:
        return redirect('transactions:statement_section_with_id', pk=first_statement.id)
    else:
        return redirect('transactions:statement_section')
    

def cash_flow_statement_view(request):
    # Get dates from GET parameters
    from_date = request.GET.get('from_date')
    through_date = request.GET.get('through_date')
    
    if from_date and through_date:
        statements = FinStatements.objects.filter(FSFromDate__gte=from_date, FSThroughDate__lte=through_date)
    else:
        # Fallback if no dates are specified; adjust as needed
        statements = FinStatements.objects.all()
    
    # Assuming you want to show the first statement as an example
    statement = statements.first()

    # If a statement is available, calculate the totals
    if statement:
        sections = StatementSections.objects.filter(FinStatementsFK=statement).prefetch_related('statementsectionlines_set__statementlineaccounts_set')
        for section in sections:
            section.total = sum(line.statementlineaccounts_set.aggregate(Sum('LAAccount')).get('LAAccount__sum', 0) for line in section.statementsectionlines_set.all())
    else:
        sections = None
    
    context = {
        'statement': statement,
        'sections': sections,
        'from_date': from_date,
        'through_date': through_date,
    }
    return render(request, 'transactions/cash_flow_statement.html', context)