from django.http import HttpResponse
from django.template import loader
from .models import PersonM, CashInAcctM
from .forms import CashInAcctMForm
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

def cashin_list(request):
    cashin_accounts = CashInAcctM.objects.all()
    return render(request, 'edit.html', {'cashin_accounts': cashin_accounts})

def cashin_add(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        description = request.POST.get('description')
        CashInAcctM.objects.create(AccountNumber=account_number, Description=description)
        return redirect('LoginRegister:cashin_list')
    return render(request, 'edit.html')

def cashin_edit(request, account_id):
    cashin_account = get_object_or_404(CashInAcctM, pk=account_id)
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        description = request.POST.get('description')
        cashin_account.AccountNumber = account_number
        cashin_account.Description = description
        cashin_account.save()
        return redirect('LoginRegister:cashin_list')
    return render(request, 'edit.html', {'cashin_account': cashin_account})

def cashin_delete(request, account_id):
    cashin_account = get_object_or_404(CashInAcctM, pk=account_id)
    if request.method == 'POST':
        cashin_account.delete()
        return redirect('LoginRegister:cashin_list')
    return render(request, 'edit.html', {'cashin_account': cashin_account})