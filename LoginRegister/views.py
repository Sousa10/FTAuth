from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import PersonM, DefaultParams, SponRates
from .forms import SponRatesForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
import os
from listsplan.models import ListHeaderT

def logout_user(request):
    logout(request)
    return redirect('members:main_menu_login')

def LoginRegister(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('base.html')
    context = {
        'FTpersons': FTpersons,
    }
    return HttpResponse(template.render(context, request))

def FTMainMenu(request):
    template = loader.get_template('LoginRegister/FTMainMenu.html')
    return HttpResponse(template.render())

def FTCalendar(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('FTCalendar.html')
    return HttpResponse(template.render())

def FTToDos(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('FTToDos.html')
    return HttpResponse(template.render())

def mainlandingpage(request):
    FTpersons = PersonM.objects.all().values()
    template = loader.get_template('main_landing_page.html')
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

def assetacctm_delete(request, pk):
    assetacctm = get_object_or_404(WhatWeOwnAcctM, pk=pk)
    assetacctm.delete()

    return redirect('LoginRegister:FTAssetAccts')

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

