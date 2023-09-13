from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'main_menu_login.html', {})

def members(request):
    return render(request, 'main_menu_login.html', {})

def main_menu_login(request):
    if request.method == "POST":
        username = request.POST[username]
        password = request.POST[password]
        user = authenticate(request, username=username, password=password)
        if  user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect(main_menu_login)
    else:
        return render(request, 'main_menu_login.html')