from django.http import HttpResponse
from django.template import loader
from .models import PersonM, CashInAcctM, CashOutAcctM, WhatWeOwnAcctM
from .models import DebtsAcctM, NetworthAcctM
from .forms import CashInAcctMForm
from .forms import CashOutAcctMForm
from .forms import WhatWeOwnAcctMForm
from .forms import DebtsAcctMForm
from .forms import EquityAcctMForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def LoginRegister(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('base.html')
  context = {
    'FTpersons': FTpersons,
  }
  return HttpResponse(template.render(context, request))

@login_required
def FTMainMenu(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTMainMenu.html')
  return HttpResponse(template.render())

def FTFinances(request):
  cashinacctms = CashInAcctM.objects.all()
  if request.method == 'POST':
        form = CashInAcctMForm(request.POST)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTFinances')    
  else:
      form = CashInAcctMForm()
  return render(request, 'FTFinances.html', {
    'form': form,
    'cashinacctms': cashinacctms,
    'title': 'Add Cash In Account',
  })

def cashinacctm_update(request, pk):
  cashinacctm = get_object_or_404(CashInAcctM, pk=pk)
  print (cashinacctm.id)
  if request.method == 'POST':
        form = CashInAcctMForm(request.POST, instance=cashinacctm)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTFinances')    
  else:
      form = CashInAcctMForm(instance=cashinacctm)
  return render(request, 'edit.html', {
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

def FTListChores(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTListChores.html')
  return HttpResponse(template.render())

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
  if request.method == 'POST':
        form = CashOutAcctMForm(request.POST)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTExpAccts')    
  else:
      form = CashOutAcctMForm()
  return render(request, 'FTExpAccts.html', {
    'form': form,
    'cashoutacctms': cashoutacctms,
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
  if request.method == 'POST':
        form = WhatWeOwnAcctMForm(request.POST)
                 
        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTAssetAccts')    
  else:
      form = WhatWeOwnAcctMForm()
  return render(request, 'FTAssetAccts.html', {
    'form': form,
    'assetacctms': assetacctms,
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
# KMS Account Groupings start Here
#