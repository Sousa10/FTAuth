from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import CashInAcctM, CashOutAcctM, WhatWeOwnAcctM, WhatWeOwnAcctM, DebtsAcctM, NetworthAcctM, PersonM
from .forms import CashInAcctMForm, EquityAcctMForm, DebtsAcctMForm, WhatWeOwnAcctMForm, CashOutAcctMForm
from django.core.paginator import Paginator
from datetime import datetime
import os
import csv

def home(request):
    return render(request, 'transactions/main_landing_page.html', {})

def main_landing_page(request):
    return render(request, 'transactions/main_landing_page.html', {})

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


# Copy from LoginRegister Starts Here

def FTFinances(request):
    cashinacctms = CashInAcctM.objects.all()
    paginator = Paginator(cashinacctms, 3)  
    page_number = request.GET.get("page")
    cashinacctms_paginated = paginator.get_page(page_number)
    if request.method == 'POST':
        print(request)
        form = CashInAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTFinances')
    else:
        form = CashInAcctMForm()
    return render(request, 'FTFinances.html', {
        'form': form,
        "cashinacctms_paginated": cashinacctms_paginated,
        'title': 'Add Cash In Account',
    })


def financesacct_update(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    print(cashinacctm.id)
    if request.method == 'POST':
        form = CashInAcctMForm(request.POST, instance=cashinacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTFinances')
    else:
        form = CashInAcctMForm(instance=cashinacctm)
    return render(request, 'FTFinances.html', {
        'form': form,
        'cashinacctm': cashinacctm,
        'title': 'Edit Cash In Account',
    })


def cashinacctm_delete(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    cashinacctm.delete()

    return redirect('transactions:income_accts')

#
#   KMS Account Groupings Starts Here
#
def FTAcctGroupings(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('FTAcctGroupings.html')
    return HttpResponse(template.render())
#
#   KMS Grouping Drill-Down Starts Here
#
def FTGroupingDrillDown(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('FTGroupingDrillDown.html')
    return HttpResponse(template.render())
#
#   KMS Account Drill-Down Starts Here
#
def FTAccountDrillDown(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('FTAccountDrillDown.html')
    return HttpResponse(template.render())
#
#   KMS Revenue Accounts Start here
#
# def FTRevenueAccts(request):
    # cashinacctms = CashInAcctM.objects.all()
    # if request.method == 'POST':
        # form = CashInAcctMForm(request.POST)

        # if form.is_valid():
            # form.save()
            # return redirect('LoginRegister:FTRevenueAccts')
    # else:
        # form = CashInAcctMForm()
    # return render(request, 'FTRevenueAccts.html', {
        # 'form': form,
        # 'cashinacctms': cashinacctms,
        # 'title': 'Add Cash In Account',
    # })


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

#
#   KMS Expense Accounts Starts here
#
def FTExpAccts(request):
    cashoutacctms = CashOutAcctM.objects.all()
    paginator = Paginator(cashoutacctms, 6)  # Show 6 accounts per page.
    page_number = request.GET.get("page")
    cashoutacctms_paginated = paginator.get_page(page_number)
    if request.method == 'POST':
        form = CashOutAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTExpAccts')
    else:
        form = CashOutAcctMForm()
    return render(request, 'FTExpAccts.html', {
        'form': form,
        'cashoutacctms_paginated': cashoutacctms_paginated,
        'title': 'Add Cash Out Account',
    })


def cashoutacctm_update(request, pk):
    cashoutacctm = get_object_or_404(CashOutAcctM, pk=pk)
    if request.method == 'POST':
        form = CashOutAcctMForm(request.POST, instance=cashoutacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTExpAccts')
    else:
        form = CashOutAcctMForm(instance=cashoutacctm)
    return render(request, 'edit_cashoutacct.html', {
        'form': form,
        'cashoutacctm': cashoutacctm,
        'title': 'Edit Cash In Account',
    })


def cashoutacctm_delete(request, pk):
    cashoutacctm = get_object_or_404(CashOutAcctM, pk=pk)
    cashoutacctm.delete()

    return redirect('LoginRegister:FTExpAccts')
#
# KMS Asset Accounts start Here
#
def FTAssetAccts(request):
    assetacctms = WhatWeOwnAcctM.objects.all()
    paginator = Paginator(assetacctms, 6)  # Show 6 accounts per page.
    page_number = request.GET.get("page")
    assetacctms_paginated = paginator.get_page(page_number)
    if request.method == 'POST':
        form = WhatWeOwnAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTAssetAccts')
    else:
        form = WhatWeOwnAcctMForm()
    return render(request, 'FTAssetAccts.html', {
        'form': form,
        'assetacctms_paginated': assetacctms_paginated,
        'title': 'Add Asset Out Account',
    })


def assetacctm_update(request, pk):
    assetacctm = get_object_or_404(WhatWeOwnAcctM, pk=pk)
    if request.method == 'POST':
        form = WhatWeOwnAcctMForm(request.POST, instance=assetacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTAssetAccts')
    else:
        form = WhatWeOwnAcctMForm(instance=assetacctm)
    return render(request, 'edit_assetacct.html', {
        'form': form,
        'assetacctm': assetacctm,
        'title': 'Edit Asset Account',
    })


def assetacctm_delete(request, pk):
    assetacctm = get_object_or_404(WhatWeOwnAcctM, pk=pk)
    assetacctm.delete()

    return redirect('LoginRegister:FTAssetAccts')
#
# KMS Liab Accounts start Here
#
def FTLiabAccts(request):
    liabacctms = DebtsAcctM.objects.all()
    if request.method == 'POST':
        form = DebtsAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTLiabAccts')
    else:
        form = DebtsAcctMForm()
    return render(request, 'FTLiabAccts.html', {
        'form': form,
        'liabacctms': liabacctms,
        'title': 'Add Liability Out Account',
    })


def liabacctm_update(request, pk):
    liabacctm = get_object_or_404(DebtsAcctM, pk=pk)
    if request.method == 'POST':
        form = DebtsAcctMForm(request.POST, instance=liabacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTLiabAccts')
    else:
        form = DebtsAcctMForm(instance=liabacctm)
    return render(request, 'edit_liabacct.html', {
        'form': form,
        'liabacctm': liabacctm,
        'title': 'Edit Liability Account',
    })


def liabacctm_delete(request, pk):
    liabacctm = get_object_or_404(DebtsAcctM, pk=pk)
    liabacctm.delete()

    return redirect('LoginRegister:FTLiabAccts')
#
# KMS Equity Accounts start Here
#
def FTEquityAccts(request):
    equityacctms = NetworthAcctM.objects.all()
    if request.method == 'POST':
        form = EquityAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTEquityAccts')
    else:
        form = EquityAcctMForm()
    return render(request, 'FTEquityAccts.html', {
        'form': form,
        'equityacctms': equityacctms,
        'title': 'Add Equity Account',
    })


def equityacctm_update(request, pk):
    equityacctm = get_object_or_404(NetworthAcctM, pk=pk)
    if request.method == 'POST':
        form = EquityAcctMForm(request.POST, instance=equityacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTEquityAccts')
    else:
        form = EquityAcctMForm(instance=equityacctm)
    return render(request, 'edit_equityacct.html', {
        'form': form,
        'equityacctm': equityacctm,
        'title': 'Edit Equity Account',
    })


def equityacctm_delete(request, pk):
    equityacctm = get_object_or_404(NetworthAcctM, pk=pk)
    equityacctm.delete()

    return redirect('LoginRegister:FTEquityAccts')

def FTEquityAccts(request):
    equityacctms = NetworthAcctM.objects.all()
    if request.method == 'POST':
        form = EquityAcctMForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTEquityAccts')
    else:
        form = EquityAcctMForm()
    return render(request, 'FTEquityAccts.html', {
        'form': form,
        'equityacctms': equityacctms,
        'title': 'Add Equity Account',
    })


def list_update(request, pk):
    equityacctm = get_object_or_404(NetworthAcctM, pk=pk)
    if request.method == 'POST':
        form = EquityAcctMForm(request.POST, instance=equityacctm)

        if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTEquityAccts')
    else:
        form = EquityAcctMForm(instance=equityacctm)
    return render(request, 'edit_equityacct.html', {
        'form': form,
        'equityacctm': equityacctm,
        'title': 'Edit Equity Account',
    })


def equityacctm_delete(request, pk):
    equityacctm = get_object_or_404(NetworthAcctM, pk=pk)
    equityacctm.delete()

    return redirect('LoginRegister:FTEquityAccts')

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
