from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import CashInAcctM, CashOutAcctM, DebtsAcctM, NetworthAcctM, PersonM, StatementLineAccounts, StatementLinesLine, StatementSections
from .forms import CashInAcctMForm
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
            paginator = Paginator(transDetail, 2)  # Show 10 ListDetailsT objects per page
            page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
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
                    paginator = Paginator(transDetail, 2)  # Show 10 ListDetailsT objects per page
                    page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
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


        ############################################
        #            NEW FROM HERE 1/14            #
        ############################################

############################################
#<<<<<<< StatementSections >>>>>>>>>>>>>>>>#
############################################

#------------------------------------------#
       # StatmentSections (HEADER) #
#------------------------------------------#
def StatementSectionsV(request, listheader_id=None):
    # listheader = None
    first_listHeader = ListHeaderT.objects.first()
    if listheader_id:
        listheader = ListHeaderT.objects.get(id=listheader_id)
        listdetails = ListDetailsT.objects.filter(ListHeaderFK=listheader)
        # Show 10 ListDetailsT objects per page
        paginator = Paginator(listdetails, 2)
        # get page number for each ListHeaderT instance
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
    else:
        listdetails = None
        page = None

    listHeaderForm = ListHeaderTForm()
    selected_header = ListHeaderT.objects.get(id=listheader_id)
    listDetailForm = ListDetailsTForm(list_header=selected_header)
    selectedHeaderForm = ListHeaderSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'ListHeaderTForm':
            listHeaderForm = ListHeaderTForm(request.POST)
            if listHeaderForm.is_valid():
                listHeaderForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'ListDetailsTForm':
            listDetailForm = ListDetailsTForm(request.POST)
            if listDetailForm.is_valid():
                listDetailForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'SelectedHeaderTForm':
            selectedHeaderForm = ListHeaderSelectForm(request.POST)
            if selectedHeaderForm.is_valid():
                listheaderName = selectedHeaderForm.cleaned_data['LHName']
                listheader = ListHeaderT.objects.get(LHName=listheaderName)
                listdetails = listheader.listdetailst_set.all()
                # Show 10 ListDetailsT objects per page
                paginator = Paginator(listdetails, 5)
                # get page number for each ListHeaderT instance
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)
                print(type(listheader.id))

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

    else:
        listHeaderForm = ListHeaderTForm()
        selected_header = ListHeaderT.objects.get(id=listheader_id)
        listDetailForm = ListDetailsTForm(list_header=selected_header)
    return render(request, 'listsplan/FTListChores.html', {
        'listHeaderForm': listHeaderForm,
        'first_listHeader': first_listHeader,
        'listDetailForm': listDetailForm,
        'selectedHeaderForm': selectedHeaderForm,
        'listheader': listheader,
        'listdetails': page,
        'title': 'List and Chores',
    })

#------------------------------------------#
    # StatmentSectionsUpdate (HEADER)
#------------------------------------------#
def StatementSections_updateV(request, pk):
    listHeader = get_object_or_404(ListHeaderT, pk=pk)
    if request.method == 'POST':
        form = ListHeaderTForm(request.POST, instance=listHeader)

        if form.is_valid():
            form.save()
            return redirect('listsplan:FTListChores', listheader_id=listHeader.id)
    else:
        form = ListHeaderTForm(instance=listHeader)
    return render(request, 'FTListChores.html', {
        'form': form,
        'listHeader': listHeader,
        'title': 'Edit Header',
    })

#------------------------------------------#
        # StatmentSectionsDelete
#------------------------------------------#
def StatementSections_deleteV(request, pk):
    listHeader = get_object_or_404(ListHeaderT, pk=pk)
    listHeader.delete()

    return redirect('listsplan:FTListChores', listheader_id=listHeader.id)

###########################################
#<<<<<<< StatementLinesLine >>>>>>>>>>>>>>#
###########################################

#------------------------------------------#
        #StatementLinesLine
#------------------------------------------#
def StatementLinesLineV(request, listheader_id=None):
    # listheader = None
    first_listHeader = ListHeaderT.objects.first()
    if listheader_id:
        listheader = ListHeaderT.objects.get(id=listheader_id)
        listdetails = ListDetailsT.objects.filter(ListHeaderFK=listheader)
        # Show 10 ListDetailsT objects per page
        paginator = Paginator(listdetails, 2)
        # get page number for each ListHeaderT instance
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
    else:
        listdetails = None
        page = None

    listHeaderForm = ListHeaderTForm()
    selected_header = ListHeaderT.objects.get(id=listheader_id)
    listDetailForm = ListDetailsTForm(list_header=selected_header)
    selectedHeaderForm = ListHeaderSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'ListHeaderTForm':
            listHeaderForm = ListHeaderTForm(request.POST)
            if listHeaderForm.is_valid():
                listHeaderForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'ListDetailsTForm':
            listDetailForm = ListDetai**lsTForm(request.POST)
            if listDetailForm.is_valid():
                listDetailForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'SelectedHeaderTForm':
            selectedHeaderForm = ListHeaderSelectForm(request.POST)
            if selectedHeaderForm.is_valid():
                listheaderName = selectedHeaderForm.cleaned_data['LHName']
                listheader = ListHeaderT.objects.get(LHName=listheaderName)
                listdetails = listheader.listdetailst_set.all()
                # Show 10 ListDetailsT objects per page
                paginator = Paginator(listdetails, 5)
                # get page number for each ListHeaderT instance
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)
                print(type(listheader.id))

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

    else:
        listHeaderForm = ListHeaderTForm()
        selected_header = ListHeaderT.objects.get(id=listheader_id)
        listDetailForm = ListDetailsTForm(list_header=selected_header)
    return render(request, 'listsplan/FTListChores.html', {
        'listHeaderForm': listHeaderForm,
        'first_listHeader': first_listHeader,
        'listDetailForm': listDetailForm,
        'selectedHeaderForm': selectedHeaderForm,
        'listheader': listheader,
        'listdetails': page,
        'title': 'List and Chores',
    })

#------------------------------------------#
        # StatementLinesLineUpdate
#------------------------------------------#
def StatementLinesLine_updateV(request, pk):
    listDetail = get_object_or_404(ListDetailsT, pk=pk)
    if request.method == 'POST':
        form = ListDetailsTForm(request.POST, instance=listDetail)

        if form.is_valid():
            form.save()
            return redirect('listsplan:FTListChores', listheader_id=listDetail.ListHeaderFK.id)
        else:
             # Log form errors
            logger.error(form.errors)
            # Print form errors to the console (for development purposes)
            print(form.errors)
            return HttpResponseServerError("Form is not valid. See server logs for details.")
    else:
        form = ListDetailsTForm(instance=listDetail)
    return render(request, 'listsplan/FTListChores.html', {
        'form': form,
        'listHeader': listDetail,
        'title': 'Edit List Detail',})

#------------------------------------------#
        # StatementLinesLineDelete
#------------------------------------------#
def StatementLinesLine_deleteV(request, pk):
    listDetail = get_object_or_404(ListDetailsT, pk=pk)
    listDetail.delete()

    return redirect('listsplan:FTListChores', listheader_id=listDetail.ListHeaderFK.id)

###########################################
#<<<<<<<  StatementLineAccounts >>>>>>>>>>#
###########################################

#------------------------------------------#
        # StatementLineAccounts
#------------------------------------------#
def StatementLineAccountsV(request, listheader_id=None):
    # listheader = None
    first_listHeader = ListHeaderT.objects.first()
    if listheader_id:
        listheader = ListHeaderT.objects.get(id=listheader_id)
        listdetails = ListDetailsT.objects.filter(ListHeaderFK=listheader)
        # Show 10 ListDetailsT objects per page
        paginator = Paginator(listdetails, 2)
        # get page number for each ListHeaderT instance
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
    else:
        listdetails = None
        page = None

    listHeaderForm = ListHeaderTForm()
    selected_header = ListHeaderT.objects.get(id=listheader_id)
    listDetailForm = ListDetailsTForm(list_header=selected_header)
    selectedHeaderForm = ListHeaderSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'ListHeaderTForm':
            listHeaderForm = ListHeaderTForm(request.POST)
            if listHeaderForm.is_valid():
                listHeaderForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'ListDetailsTForm':
            listDetailForm = ListDetai**lsTForm(request.POST)
            if listDetailForm.is_valid():
                listDetailForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'SelectedHeaderTForm':
            selectedHeaderForm = ListHeaderSelectForm(request.POST)
            if selectedHeaderForm.is_valid():
                listheaderName = selectedHeaderForm.cleaned_data['LHName']
                listheader = ListHeaderT.objects.get(LHName=listheaderName)
                listdetails = listheader.listdetailst_set.all()
                # Show 10 ListDetailsT objects per page
                paginator = Paginator(listdetails, 5)
                # get page number for each ListHeaderT instance
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)
                print(type(listheader.id))

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

    else:
        listHeaderForm = ListHeaderTForm()
        selected_header = ListHeaderT.objects.get(id=listheader_id)
        listDetailForm = ListDetailsTForm(list_header=selected_header)
    return render(request, 'listsplan/FTListChores.html', {
        'listHeaderForm': listHeaderForm,
        'first_listHeader': first_listHeader,
        'listDetailForm': listDetailForm,
        'selectedHeaderForm': selectedHeaderForm,
        'listheader': listheader,
        'listdetails': page,
        'title': 'List and Chores',
    })

#------------------------------------------#
        # StatementLineAccountsUpdate
#------------------------------------------#
def StatementLineAccounts_updateV(request, pk):
    listHeader = get_object_or_404(ListHeaderT, pk=pk)
    if request.method == 'POST':
        form = ListHeaderTForm(request.POST, instance=listHeader)

        if form.is_valid():
            form.save()
            return redirect('listsplan:FTListChores', listheader_id=listHeader.id)
    else:
        form = ListHeaderTForm(instance=listHeader)
    return render(request, 'FTListChores.html', {
        'form': form,
        'listHeader': listHeader,
        'title': 'Edit Header',
    })

#------------------------------------------#
        # StatementLineAccountsDelete
#------------------------------------------#
def StatementLineAccounts_deleteVz(request, pk):
    listDetail = get_object_or_404(ListDetailsT, pk=pk)
    listDetail.delete()

    return redirect('listsplan:FTListChores', listheader_id=listDetail.ListHeaderFK.id)