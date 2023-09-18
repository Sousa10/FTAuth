from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'members/main_menu_login.html', {})

# def members(request):
    # return render(request, 'members/main_menu_login.html', {})

def main_menu_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if  user is not None:
            login(request, user)
            return redirect('LoginRegister:FTMainMenu')
        else:
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect('main_menu_login')
    else:
        return render(request, 'members/main_menu_login.html')
    
def register_user(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)    
            login(request, user)
            return redirect('LoginRegister:FTMainMenu')
    else:
        form = UserCreationForm()
    
    return render(request, 'members/register_user.html', {
        'form':form,  
        })

def logout_user(request):
    logout(request)
    print("in logout")
    return redirect('members:main_menu_login')