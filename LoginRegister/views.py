from django.http import HttpResponse
from django.template import loader
from .models import PersonM, CashInAcctM, CashOutAcctM, WhatWeOwnAcctM, ListHeaderT, ListDetailsT, TransBatch, TransDetail, TransHeader, DefaultParams, SponRates, DebtsAcctM, NetworthAcctM
from .forms import ListHeaderTForm, ListDetailsTForm, ListHeaderSelectForm, UploadExcelForm, ListHeaderTForm, ListDetailsTForm, SponRatesForm, EquityAcctMForm, DebtsAcctMForm, WhatWeOwnAcctMForm, CashOutAcctMForm, CashInAcctMForm, TransBatchForm, TemplateActionForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
import openpyxl, os
from io import BytesIO

def LoginRegister(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('base.html')
  context = {
    'FTpersons': FTpersons,
  }
  return HttpResponse(template.render(context, request))

#@login_required
def FTMainMenu(request):
  listHeader = ListHeaderT.objects.first()
  template = loader.get_template('FTMainMenu.html')
  context = {
    'listHeader': listHeader,
  }
  return HttpResponse(template.render(context, request))

def FTFinances(request):
  cashinacctms = CashInAcctM.objects.all()
  paginator = Paginator(cashinacctms, 3)  # Show 25 contacts per page.
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
  print (cashinacctm.id)
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

  return redirect('LoginRegister:FTFinances')

def FTCalendar(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTCalendar.html')
  return HttpResponse(template.render())

def FTToDos(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTToDos.html')
  return HttpResponse(template.render())

def FTListChores(request, listheader_id=None):
  #listheader = None
  if listheader_id:
    listheader = ListHeaderT.objects.get(id=listheader_id)
    listdetails = ListDetailsT.objects.filter(ListHeaderFK=listheader)
    paginator = Paginator(listdetails, 2)  # Show 10 ListDetailsT objects per page
    page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
    page = paginator.get_page(page_number)
  else:
    listdetails = None
    page = None
  
  listHeaderForm = ListHeaderTForm()
  selected_header = ListHeaderT.objects.get(id=listheader_id)
  listDetailForm = ListDetailsTForm(list_header = selected_header)
  selectedHeaderForm = ListHeaderSelectForm()

  if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'ListHeaderTForm':
          listHeaderForm = ListHeaderTForm(request.POST)
          if listHeaderForm.is_valid():
             listHeaderForm.save()

             return redirect('LoginRegister:FTListChores', listheader_id=listheader.id)
          
        elif form_type == 'ListDetailsTForm':
          listDetailForm = ListDetailsTForm(request.POST)
          if listDetailForm.is_valid():
            listDetailForm.save()

            return redirect('LoginRegister:FTListChores', listheader_id=listheader.id)
          
        elif form_type == 'SelectedHeaderTForm':
          print(form_type)
          selectedHeaderForm = ListHeaderSelectForm(request.POST)
          if selectedHeaderForm.is_valid():
            listheaderName = selectedHeaderForm.cleaned_data['LHName']
            listheader = ListHeaderT.objects.get(LHName=listheaderName)
            listdetails = listheader.listdetailst_set.all()
            paginator = Paginator(listdetails, 5)  # Show 10 ListDetailsT objects per page
            page_number = request.GET.get('page', 1)  # get page number for each ListHeaderT instance
            page = paginator.get_page(page_number)
            print(type(listheader))

            return redirect('LoginRegister:FTListChores', listheader_id=listheader.id)

            # return render(request, 'FTListChores.html', {
            #   'listHeaderForm': listHeaderForm,
            #   'listDetailForm': listDetailForm,
            #   'selectedHeaderForm': selectedHeaderForm,
            #   'listheader': listheader,
            #   'listdetails': page,
            # })
  else:
      listHeaderForm = ListHeaderTForm()
      selected_header = ListHeaderT.objects.get(id=listheader_id)
      listDetailForm = ListDetailsTForm(list_header = selected_header)
  return render(request, 'FTListChores.html', {
    'listHeaderForm': listHeaderForm,
    'listDetailForm': listDetailForm,
    'selectedHeaderForm': selectedHeaderForm,
    'listheader': listheader,
    'listdetails': page,
    'title': 'List and Chores',
  })

def listHeader_update(request, pk):
  listHeader = get_object_or_404(ListHeaderT, pk=pk)
  if request.method == 'POST':
        form = ListHeaderTForm(request.POST, instance=listHeader)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTListChores', listheader_id=listHeader.id)    
  else:
      form = ListHeaderTForm(instance=listHeader)
  return render(request, 'FTListChores.html', {
    'form': form,
    'listHeader': listHeader,
    'title': 'Edit Header',
  })
def listDetail_update(request, pk):
  listDetail = get_object_or_404(ListDetailsT, pk=pk)
  if request.method == 'POST':
        form = ListDetailsTForm(request.POST, instance=listDetail)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTListChores', listheader_id=listDetail.ListHeaderFK.id)    
  else:
      form = ListDetailsTForm(instance=listDetail)
  return render(request, 'FTListChores.html', {
    'form': form,
    'listHeader': listDetail,
    'title': 'Edit List Detail',
  })

def listHeader_delete(request, pk):
  listHeader = get_object_or_404(ListHeaderT, pk=pk)
  listHeader.delete()

  return redirect('LoginRegister:FTListChores', listheader_id=listHeader.id)

def listDetail_delete(request, pk):
  listDetail = get_object_or_404(ListDetailsT, pk=pk)
  listDetail.delete()

  return redirect('LoginRegister:FTListChores', listheader_id=listDetail.ListHeaderFK.id)

def FTFamilyTracks(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTFamilyTracks.html')
  return HttpResponse(template.render())

def FTFitnessSports(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTFitnessSports.html')
  return HttpResponse(template.render())

def FTGrocery(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTGrocery.html')
  return HttpResponse(template.render())

def FTAcministration(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTAcministration.html')
  return HttpResponse(template.render())

def FTFinancesMenu(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTFinancesMenu.html')
  return HttpResponse(template.render())

def FTFinMenu(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTFinMenu.html')
  return HttpResponse(template.render())

def FTDefAcctsMenu(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTDefAcctsMenu.html')
  return HttpResponse(template.render())
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
def FTRevenueAccts(request):
  cashinacctms = CashInAcctM.objects.all()
  if request.method == 'POST':
        form = CashInAcctMForm(request.POST)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTRevenueAccts')    
  else:
      form = CashInAcctMForm()
  return render(request, 'FTRevenueAccts.html', {
    'form': form,
    'cashinacctms': cashinacctms,
    'title': 'Add Cash In Account',
  })

def cashinacctm_update(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    if request.method == 'POST':
          form = CashInAcctMForm(request.POST, instance=cashinacctm)
          if form.is_valid():
            form.save()
            return redirect('LoginRegister:FTRevenueAccts')    
    else:
        form = CashInAcctMForm(instance=cashinacctm)
    return render(request, 'edit_cashinacct.html', {
      'form': form,
      'cashinacctm': cashinacctm,
      'title': 'Edit Cash In Account',
    })

def cashinacctm_delete(request, pk):
    cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
    cashinacctm.delete()

    return redirect('LoginRegister:FTRevenueAccts')

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
    'assetacctms_paginated' : assetacctms_paginated,
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

# 
# KMS List & Chores start Here
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
# 
# KMS Family Security start Here
#
def FTFamilySecurity(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTFamilySecurity.html')
  return HttpResponse(template.render())
# 
# KMS Apple start Here
#
def FTApple(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTApple.html')
  return HttpResponse(template.render())
# 
# KMS Android start Here
#
def FTAndroid(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTAndroid.html')
  return HttpResponse(template.render())
# 
#   KMS Sponsor Rate Table Starts here
# 
def FTSponRateTbl(request):
  sponratesms = SponRates.objects.all()
  paginator = Paginator(sponratesms, 11)  # Show 11 accounts per page.
  page_number = request.GET.get("page")
  sponratesms_paginated = paginator.get_page(page_number)
  if request.method == 'POST':
        form = SponRatesForm(request.POST)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTSponRateTbl')    
  else:
      form = SponRatesForm(), 
  return render(request, 'FTSponRateTbl.html', {
    'form': form,
    'sponratesms_paginated': sponratesms_paginated,
    'title': 'Sponsor Rates',
  })
# 
# New 8/16 Start here, drop boxes for Calendar template
# 
class DefaultParamsViewCreate():
    template_name = 'fafl/defaultSquad_form.html'
    model = DefaultParams
    fields = ['Calendar', 'View', 'Date']
    # success_url = reverse_lazy('fafl:DefaultParams-list')

    # def get_context_data(self, **kwargs):
        # context = super(DefaultParamsView, self).get_context_data(**kwargs)
        # context['clubs'] = Clubs.objects.all().order_by('club_id')
        # context['players'] = Players.objects.all().order_by('player_id')
        # return context
def populate_from_csv(excel_file, trans_batch):
    workbook = openpyxl.load_workbook(filename=BytesIO(excel_file.read()))
    sheet = workbook.active
    current_header = None

    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skipping header
        TransDescription, TransDate, TransNote, AccountNumber, Description, DrAmount, CrAmount = row

        # If TransDescription is present, create a new TransHeader record.
        if TransDescription:
            current_header = TransHeader.objects.create(
                TransBatchID=trans_batch,
                TransDescription=TransDescription,
                TransDate=TransDate,
                TransNote=TransNote
            )
        if current_header:
            TransDetail.objects.create(
                TransHeaderID=current_header,
                AccountNumber=AccountNumber,
                Description=Description,
                DrAmount=DrAmount,
                CrAmount=CrAmount
            )

def FTTransactions(request):
    if request.method == 'POST':
      # batchForm = TransBatchForm(request.POST)
      # excelForm = UploadExcelForm(request.POST, request.FILES)
      form = TemplateActionForm(request.POST, request.FILES)
      
      if form.is_valid():
          #trans_batch = batchForm.save()
          if form.cleaned_data['action'] == 'download':
              # Use the pre-existing Excel file for download
            filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "template.csv")
            with open(filename, "rb") as excel:
                response = HttpResponse(excel.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
          
          elif form.cleaned_data['action'] == 'upload':
             excel_file = request.FILES['excel_file']
          # if excelForm.is_valid():
          #   excel_file = request.FILES['excel_file']
          #   #populate_from_excel(excel_file, trans_batch)
          #   return redirect('LoginRegister:FTTransactions')  # Redirect back to the same view
    else:
      form = TemplateActionForm()
      # batchForm = TransBatchForm()
      # excelForm = UploadExcelForm()

    transactions = TransDetail.objects.all()
    # Assuming you want to display all the batches, headers, and details on the same page
    batches = TransBatch.objects.all()
    paginator = Paginator(transactions, 11)  # Show 11 accounts per page.
    page_number = request.GET.get("page")
    transactions_paginated = paginator.get_page(page_number)
    context = {
      # 'batchForm': batchForm,
      # 'excelForm': excelForm,
      'form': form,
      'transactions': transactions_paginated,
      'batches': batches
    }
    return render(request, 'FTTransactions.html', context)

def transaction_delete(request, pk):
    transaction = get_object_or_404(TransDetail, pk=pk)
    transaction.delete()

    return redirect('LoginRegister:FTTransactions')