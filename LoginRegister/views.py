from django.http import HttpResponse
from django.template import loader
from .models import PersonM, CashInAcctM, CashOutAcctM, WhatWeOwnAcctM
from .forms import CashInAcctMForm
from .forms import CashOutAcctMForm
from .forms import WhatWeOwnAcctMForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def LoginRegister(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTperson_login.html')
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
# KMS start Here
# 
# def FTAssetAccts(request):
  # assetacctms = WhatWeOwnAcctM.objects.all()
  # if request.method == 'POST':
        # form = CashOutAcctMForm(request.POST)

        # if form.is_valid():
          # form.save()
          # return redirect('LoginRegister:FTExpAccts')    
  # else:
      # form = CashOutAcctMForm()
  # return render(request, 'FTExpAccts.html', {
    # 'form': form,
    # 'cashoutacctms': cashoutacctms,
    # 'title': 'Add Cash Out Account',
  # })

# def cashoutacctm_update(request, pk):
    # cashoutacctm = get_object_or_404(CashOutAcctM, pk=pk)
    # if request.method == 'POST':
          # form = CashOutAcctMForm(request.POST, instance=cashoutacctm)

          # if form.is_valid():
            # form.save()
            # return redirect('LoginRegister:FTExpAccts')    
    # else:
        # form = CashOutAcctMForm(instance=cashoutacctm)
    # return render(request, 'edit_cashoutacct.html', {
      # 'form': form,
      # 'cashoutacctm': cashoutacctm,
      # 'title': 'Edit Cash In Account',
    # })

# def cashoutacctm_delete(request, pk):
    # cashoutacctm = get_object_or_404(CashOutAcctM, pk=pk)
    # cashoutacctm.delete()

    # return redirect('LoginRegister:FTExpAccts')