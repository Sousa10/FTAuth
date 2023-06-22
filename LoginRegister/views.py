from django.http import HttpResponse
from django.template import loader
from .models import PersonM
from .forms import CashInAcctMForm
from django.shortcuts import render, redirect

def LoginRegister(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTperson_login.html')
  context = {
    'FTpersons': FTpersons,
  }
  return HttpResponse(template.render(context, request))

def FTMainMenu(request):
  FTpersons = PersonM.objects.all().values()
  template = loader.get_template('FTMainMenu.html')
  return HttpResponse(template.render())

def FTFinances(request):
  if request.method == 'POST':
        form = CashInAcctMForm(request.POST)

        if form.is_valid():
          form.save()
          return redirect('LoginRegister:FTFinances')    
  else:
      form = CashInAcctMForm()
  return render(request, 'FTFinances.html', {
    'form': form,
  })

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
