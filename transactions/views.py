from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import CashInAcctM, FinStatements, PersonM, StatementLineAccounts, StatementLinesLine, StatementSections
from .forms import CashInAcctMForm, StatementLineAccountsForm, StatementSectionsForm, StatementLinesLineForm
from django.core.paginator import Paginator
from datetime import datetime
import os
from LoginRegister.utils import increment_click_count
from django.http import HttpResponseServerError
import logging
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
    # reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
    # print(reader)
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

def home(request):
    name = "Kirk"
    return render(request,
                  'home.html', {
                      'name': name
                  })

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
    






############################################
#<<<<<<< StatementSections >>>>>>>>>>>>>>>>#
############################################
#------------------------------------------#
       # StatementSectionsV 
#------------------------------------------#
def StatementSectionsV(request):
    ssections = StatementSections.objects.all()

    if request.method == 'POST':
        form = StatementSectionsForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('transations:sections')

    else:

        form = StatementSectionsForm()

    return render(request, 'transations:sections.html', {
        'form': form,
        'ssections': ssections,
        'title': 'Sections'
    })

#------------------------------------------#
    # StatementSections_updateV
#------------------------------------------#
def StatementSections_updateV(request, pk):
    ssection = get_object_or_404(StatementSections, pk=pk)
    if request.method == 'POST':
        form = StatementSectionsForm(request.POST, instance=ssection)

        if form.is_valid():
            form.save()
            return redirect('transations:sections', section_id=StatementSections.id)
    else:
        form = StatementSectionsForm(instance=ssection)

    return render(request, 'sections.html', {
        'form': form,
        'ssection': ssection,
        'title': 'Update Section'
    })

#------------------------------------------#
        # StatmentSectionsDelete
#------------------------------------------#
def StatementSections_deleteV(request, pk):
    ssection = get_object_or_404(StatementSections, pk=pk)
    ssection.delete()

    return redirect('listsplan:FTListChores', sectionheader_id=listHeader.id)

############################################
#<<<<<<< StatementLinesLine >>>>>>>>>>>>>>>#
############################################
#------------------------------------------#
        # StatementLinesLineV
#------------------------------------------#
def StatementLinesLineV(request):
    sllines = StatementLinesLine.objects.all()

    if request.method == 'POST':
        form = StatementLinesLineForm(request.post)

        if form.is_valid():
                form.save()
                return redirect('transactions:statement_lines')

    else:

        form = StatementLinesLineForm()

    return render(request, 'transactions:statement_lines.html', {
        'form': form,
        'sllines': sllines,
        'title': 'Statement Lines',
    })

#------------------------------------------#
        # StatementLinesLineUpdate
#------------------------------------------#
def StatementLinesLine_updateV(request, pk):
    slline = get_object_or_404(StatementLinesLine, pk=pk)
    if request.method == 'POST':
        form = StatementLinesLineForm(request.POST, instance=slline)
        if form.is_valid():
            form.save()
            return redirect('transactions:statement_lines')
    else:
        form = StatementLinesLineForm(instance=slline)
    return render(request, 'transactions:statement_lines.html', {
        'form': form,
        'sllines': slline,
        'title': 'Statement Lines',
    })

#------------------------------------------#
        # StatementLinesLineDelete
#------------------------------------------#
def StatementLinesLine_deleteV(request, pk):
    listDetail = get_object_or_404(StatementLinesLine, pk=pk)
    listDetail.delete()

    return redirect('transactions:statement_lines')

############################################
#<<<<<<< Statement Line Accounts >>>>>>>>>>#
############################################
#------------------------------------------#
#          StatementLineAccountsV           
#------------------------------------------#
def StatementLineAccountsV(request):
    slaccounts = StatementLineAccounts.objects.all()
    if request.method == 'POST':
        form = StatementLineAccountsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transactions:accounts')
    else:
        form = StatementLineAccountsForm()
    return render(request, 'transactions/accounts.html', {
        'form': form,
        'slaccounts': slaccounts,
        'title': 'Add Account',
    })

#------------------------------------------#
#      StatementLineAccounts_updateV           
#------------------------------------------#
def StatementLineAccounts_updateV(request, pk):
    slaccount = get_object_or_404(StatementLineAccounts, pk=pk)
    if request.method == 'POST':
        form = StatementLineAccountsForm(request.POST, instance=slaccount)
        if form.is_valid():
            form.save()
            return redirect('transactions:income_accts')
    else:
        form = StatementLineAccountsForm(instance=slaccount)
    return render(request, 'transactions/FTRevenueAccts.html', {
        'form': form,
        'slaccount': slaccount,
        'title': 'Edit Account',
    })

#------------------------------------------#
#      StatementLineAccounts_deleteV           
#------------------------------------------#
def StatementLineAccounts_deleteV(request, pk):
    slaccounts = get_object_or_404(StatementLineAccounts, pk=pk)
    slaccounts.delete()

    return redirect('transactions:accounts')

#######################################################################
#<<<<    O L D   O L D   O L D   O L D   O L D   O L D   O L D    >>>>#
#######################################################################
#------------------------------------------#
        # StatementLineAccounts
#------------------------------------------#
# def StatementLineAccountsV(request, sectionheader_id=None):
    # sectionheader = None
    # first_listHeader = StatementSections.objects.first()
    # if sectionheader_id:
        # sectionheader = StatementSections.objects.get(id=sectionheader_id)
        # listdetails = StatementLinesLine.objects.filter(ListHeaderFK=sectionheader)
        # Show 10 StatementLinesLine objects per page
        # paginator = Paginator(listdetails, 2)
        # get page number for each StatementSections instance
        # page_number = request.GET.get('page', 1)
        # page = paginator.get_page(page_number)
    # else:
        # listdetails = None
        # page = None

    # listHeaderForm = StatementSectionsForm()
    # selected_header = StatementSections.objects.get(id=sectionheader_id)
    # listDetailForm = StatementLinesLineForm(list_header=selected_header)
    # selectedHeaderForm = ListHeaderSelectForm()

    # if request.method == 'POST':
        # form_type = request.POST.get('form_type')
        # if form_type == 'StatementSectionsForm':
            # listHeaderForm = StatementSectionsForm(request.POST)
            # if listHeaderForm.is_valid():
                # listHeaderForm.save()

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

        # elif form_type == 'StatementLinesLineForm':
            # listDetailForm = ListDetai**lsTForm(request.POST)
            # if listDetailForm.is_valid():
                # listDetailForm.save()

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

        # elif form_type == 'SelectedHeaderTForm':
            # selectedHeaderForm = ListHeaderSelectForm(request.POST)
            # if selectedHeaderForm.is_valid():
                # sectionheaderName = selectedHeaderForm.cleaned_data['LHName']
                # sectionheader = StatementSections.objects.get(LHName=sectionheaderName)
                # listdetails = sectionheader.listdetailst_set.all()
                # Show 10 StatementLinesLine objects per page
                # paginator = Paginator(listdetails, 5)
                # get page number for each StatementSections instance
                # page_number = request.GET.get('page', 1)
                # page = paginator.get_page(page_number)
                # print(type(sectionheader.id))

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

    # else:
        # listHeaderForm = StatementSectionsForm()
        # selected_header = StatementSections.objects.get(id=sectionheader_id)
        # listDetailForm = StatementLinesLineForm(list_header=selected_header)
    # return render(request, 'listsplan/FTListChores.html', {
        # 'listHeaderForm': listHeaderForm,
        # 'first_listHeader': first_listHeader,
        # 'listDetailForm': listDetailForm,
        # 'selectedHeaderForm': selectedHeaderForm,
        # 'sectionheader': sectionheader,
        # 'listdetails': page,
        # 'title': 'List and Chores',
    # })

#------------------------------------------#
        # StatementLineAccountsUpdate
#------------------------------------------#
# def StatementLineAccounts_updateV(request, pk):
    # listHeader = get_object_or_404(StatementSections, pk=pk)
    # if request.method == 'POST':
        # form = StatementSectionsForm(request.POST, instance=listHeader)

        # if form.is_valid():
            # form.save()
            # return redirect('listsplan:FTListChores', sectionheader_id=listHeader.id)
    # else:
        # form = StatementSectionsForm(instance=listHeader)
    # return render(request, 'FTListChores.html', {
        # 'form': form,
        # 'listHeader': listHeader,
        # 'title': 'Edit Header',
    # })

#------------------------------------------#
        # StatementLineAccountsDelete
#------------------------------------------#
# def StatementLineAccounts_deleteV(request, pk):
    # listDetail = get_object_or_404(StatementLinesLine, pk=pk)
    # listDetail.delete()

    # return redirect('listsplan:FTListChores', sectionheader_id=listDetail.ListHeaderFK.id)

#------------------------------------------#
        #StatementLinesLine
#------------------------------------------#
# def StatementLinesLineV(request, sectionheader_id=None):
    # sectionheader = None
    # first_listHeader = StatementSections.objects.first()
    # if sectionheader_id:
        # sectionheader = StatementSections.objects.get(id=sectionheader)
        # listdetails = StatementLinesLine.objects.filter(ListHeaderFK=sectionheader)
        # Show 10 StatementLinesLine objects per page
        # paginator = Paginator(listdetails, 2)
        # get page number for each StatementSections instance
        # page_number = request.GET.get('page', 1)
        # page = paginator.get_page(page_number)
    # else:
        # listdetails = None
        # page = None

    # listHeaderForm = StatementSectionsForm()
    # selected_header = StatementSections.objects.get(id=sectionheader_id)
    # listDetailForm = StatementLinesLineForm(list_header=selected_header)
    # selectedHeaderForm = ListHeaderSelectForm()

    # if request.method == 'POST':
        # form_type = request.POST.get('form_type')
        # if form_type == 'StatementSectionsForm':
            # listHeaderForm = StatementSectionsForm(request.POST)
            # if listHeaderForm.is_valid():
                # listHeaderForm.save()

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

        # elif form_type == 'StatementLinesLineForm':
            # listDetailForm = ListDetai**lsTForm(request.POST)
            # if listDetailForm.is_valid():
                # listDetailForm.save()

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

        # elif form_type == 'SelectedHeaderTForm':
            # selectedHeaderForm = ListHeaderSelectForm(request.POST)
            # if selectedHeaderForm.is_valid():
                # sectionheaderName = selectedHeaderForm.cleaned_data['LHName']
                # sectionheader = StatementSections.objects.get(LHName=sectionheaderName)
                # listdetails = sectionheader.listdetailst_set.all()
                # Show 10 StatementLinesLine objects per page
                # paginator = Paginator(listdetails, 5)
                # get page number for each StatementSections instance
                # page_number = request.GET.get('page', 1)
                # page = paginator.get_page(page_number)
                # print(type(sectionheader.id))

                # return redirect('listsplan:FTListChores', sectionheader_id=sectionheader.id)

    # else:
        # listHeaderForm = StatementSectionsForm()
        # selected_header = StatementSections.objects.get(id=sectionheader_id)
        # listDetailForm = StatementLinesLineForm(list_header=selected_header)
    # return render(request, 'listsplan/FTListChores.html', {
        # 'listHeaderForm': listHeaderForm,
        # 'first_listHeader': first_listHeader,
        # 'listDetailForm': listDetailForm,
        # 'selectedHeaderForm': selectedHeaderForm,
        # 'sectionheader': sectionheader,
        # 'listdetails': page,
        # 'title': 'List and Chores',
    # })

#------------------------------------------#
        # StatementLinesLineUpdate
#------------------------------------------#
# def StatementLinesLine_updateV(request, pk):
    # listDetail = get_object_or_404(StatementLinesLine, pk=pk)
    # if request.method == 'POST':
        # form = StatementLinesLineForm(request.POST, instance=listDetail)

        # if form.is_valid():
            # form.save()
            # return redirect('listsplan:FTListChores', sectionheader_id=listDetail.ListHeaderFK.id)
        # else:
             # Log form errors
            # logger.error(form.errors)
            # Print form errors to the console (for development purposes)
            # print(form.errors)
            # return HttpResponseServerError("Form is not valid. See server logs for details.")
    # else:
        # form = StatementLinesLineForm(instance=listDetail)
    # return render(request, 'listsplan/FTListChores.html', {
        # 'form': form,
        # 'listHeader': listDetail,
        # 'title': 'Edit List Detail',})

#------------------------------------------#
        # StatementLinesLineDelete
#------------------------------------------#
# def StatementLinesLine_deleteV(request, pk):
    # listDetail = get_object_or_404(StatementLinesLine, pk=pk)
    # listDetail.delete()

    # return redirect('listsplan:FTListChores', sectionheader_id=listDetail.ListHeaderFK.id)

# 1_21 def populate_from_csv(csv_file):
    # reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
    # print(reader)
# 1_21     file_data = csv_file.read().decode("utf-8")
# 1_21     csv_data = file_data.split("\n")
# 1_21     for row in csv_data:
# 1_21         # Skip empty rows
# 1_21         if not row.strip():
# 1_21             continue
# 1_21         fields = row.split(",")
        # print(len(fields))
# 1_21         if len(fields) < 7:  # Adjust this number based on the minimum columns you expect
# 1_21             continue

# 1_21         formatted_date = None
        # If TransDescription is present, create a new TransHeader record.
# 1_21         if fields[0] == 'TB' and fields[2] and fields[4]:
# 1_21             if fields[4]:
# 1_21                 try:
# 1_21                     formatted_date = format_date(fields[4])
# 1_21                     trans_batch = TransBatch.objects.create(
# 1_21                         TransBatchName=fields[2], TransBatchDate=formatted_date or None)
# 1_21                 except ValueError:
                    # Handle or log the malformed date value here
# 1_21                     print(f"Invalid date format for entry: {fields[4]}")

# 1_21         elif fields[0] == 'TH' and fields[3] and fields[5] and fields[7]:
# 1_21             if fields[5]:
# 1_21              try:
# 1_21                        formatted_date = format_date(fields[5])
# 1_21                     current_header = TransHeader.objects.create(
# 1_21                         TransBatchID=trans_batch,
# 1_21                         TransDescription=fields[3],
# 1_21                         TransDate=formatted_date,
# 1_21                         TransNote=fields[7]
# 1_21                     )
# 1_21                 except ValueError:
                    # Handle or log the malformed date value here
# 1_21                     print(f"Invalid date format for entry: {fields[5]}")

# 1_21         elif fields[0] == 'TD' and fields[2]:
# 1_21             try:
# 1_21                 amount = int(fields[2])
# 1_21                 TransDetail.objects.create(
# 1_21                     TransHeaderID=current_header,
# 1_21                     Amount=amount,
# 1_21                     DrAccount=fields[4],
# 1_21                     CrAccount=fields[6]
# 1_21                 )
# 1_21             except ValueError:
# 1_21                 print(f"Invalid amount format for entry: {fields[2]}")

# 1_21 def FTTransactions(request, batch_id=None):
# 1_21     if batch_id:
# 1_21         transBatch = TransBatch.objects.get(id=batch_id)
# 1_21         transHeaders = transBatch.transheader_set.all()
# 1_21         for transHeader in transHeaders:
# 1_21             transDetail = transHeader.transdetail_set.all()
# 1_21             paginator = Paginator(transDetail, 2)  # Show 10 ListDetailsT objects per page
# 1_21             page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
# 1_21             page = paginator.get_page(page_number)
# 1_21     else:
# 1_21       transDetail = None
# 1_21       page = None
    
# 1_21     transBatch = TransBatch.objects.first()
# 1_21     form = TemplateActionForm()
# 1_21     transbatchForm = TransBatchSelectForm()

# 1_21     if request.method == 'POST':
# 1_21         form_type = request.POST.get('form_type')
# 1_21         if form_type == 'uploadDownload':
# 1_21             form = TemplateActionForm(request.POST, request.FILES)
# 1_21             if form.is_valid():
# 1_21                 if form.cleaned_data['action'] == 'download':
# 1_21                     # Use the pre-existing Excel file for download
# 1_21                     filename = os.path.join(os.path.dirname(
# 1_21                         os.path.dirname(__file__)), "resources", "template.xlsx")
# 1_21                     with open(filename, "rb") as excel:
# 1_21                         response = HttpResponse(
# 1_21                             excel.read(), content_type='application/vnd.ms-excel')
# 1_21                         response['Content-Disposition'] = 'inline; filename=' + \
# 1_21                             os.path.basename(filename)
# 1_21                     return response
 
# 1_21                 elif form.cleaned_data['action'] == 'upload':
# 1_21                     csv_file = request.FILES['excel_file']
# 1_21                     if not csv_file.name.endswith('.csv'):
# 1_21                         print("whatt!!!!")
# 1_21                         messages.warning(
# 1_21                             request, 'The wrong file type was uploaded')
# 1_21                         return HttpResponseRedirect(request.path_info)
# 1_21                     populate_from_csv(csv_file)
                    # Redirect back to the same view
# 1_21                     return redirect('LoginRegister:FTTransactions', batch_id = transBatch.id)
# 1_21         elif form_type == 'SelectedBatchForm':
# 1_21             transbatchForm = TransBatchSelectForm(request.POST)
# 1_21             if transbatchForm.is_valid():
# 1_21                 batchname = transbatchForm.cleaned_data['BatchName']
# 1_21                 transbatch = TransBatch.objects.get(TransBatchName=batchname)
# 1_21                 print(transbatch.id)
# 1_21                 transHeaders = transBatch.transheader_set.all()
# 1_21                 for transHeader in transHeaders:
# 1_21                     transDetail = transHeader.transdetail_set.all()
# 1_21                     paginator = Paginator(transDetail, 2)  # Show 10 ListDetailsT objects per page
# 1_21                     page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
# 1_21                     page = paginator.get_page(page_number)
# 1_21                     return redirect('LoginRegister:FTTransactions', batch_id = transbatch.id)

# 1_21     else:
# 1_21         form = TemplateActionForm()
# 1_21         transbatchForm = TransBatchSelectForm()

# 1_21     transactions = TransDetail.objects.all()
    # Assuming you want to display all the batches, headers, and details on the same page
# 1_21     batch = TransBatch.objects.all()
# 1_21     paginator = Paginator(transactions, 11)  # Show 11 accounts per page.
# 1_21     page_number = request.GET.get("page")
# 1_21     transactions_paginated = paginator.get_page(page_number)
# 1_21     context = {
# 1_21         'form': form,
# 1_21         'transactions': transactions_paginated,
        # 'batch': batch,
# 1_21         'transBatch': transBatch,
# 1_21         'transbatchForm': transbatchForm,
# 1_21         'transdetail': page
# 1_21     }
# 1_21     return render(request, 'LoginRegister/FTTransactions.html', context)


# 1_21 def transaction_delete(request, pk):
# 1_21     transaction = get_object_or_404(TransDetail, pk=pk)
# 1_21     transaction.delete()

# 1_21     return redirect('LoginRegister:FTTransactions')
