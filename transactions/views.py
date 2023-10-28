from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import CashInAcctM
from .forms import CashInAcctMForm

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
            return redirect('LoginRegister:FTRevenueAccts')
    else:
        form = CashInAcctMForm()
    return render(request, 'FTRevenueAccts.html', {
        'form': form,
        'cashinacctms': cashinacctms,
        'title': 'Add Cash In Account',
    })
