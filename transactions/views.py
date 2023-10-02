from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'transactions/main_landing_page.html', {})

def main_landing_page(request):
    return render(request, 'transactions/main_landing_page.html', {})