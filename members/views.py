from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UpdateUserForm
from django.contrib.auth.models import User
from familytracks.models import Profile
from familytracks.forms import ProfilePicForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .backends import CustomModelBackend


def home(request):
    return render(request, 'members/main_menu_login.html', {})

# def members(request):
    # return render(request, 'members/main_menu_login.html', {})

class ChangePasswordView(PasswordChangeView):
    template_name = 'members/change_password.html'
    success_url = reverse_lazy('LoginRegister:FTMainMenu')

def main_menu_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, backend=CustomModelBackend)
        if  user is not None:
            login(request, user)
            print(dict(request.session))
            # if not user.password_changed:
            #     user.password_changed = True
            #     user.save()
            if request.session['first_login'] == False:
                print("this user has logged in before")
            else:
                print("this is the first login by this user")
                # Perform actions before last_login is updated
                request.session['first_login'] = False
                return redirect('members:change_password')
            # if request.session.get('first_login'):
            #     print("OKKKKKK")
            #     # Clear the session attribute to prevent redirection on subsequent logins
            #     request.session.pop('first_login', None)
            #     return redirect('members:change_password')
            return redirect('LoginRegister:FTMainMenu')
        else:
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect('members:main_menu_login')
    else:
        return render(request, 'members/main_menu_login.html')
    
def logout_user(request):
    logout(request)
    return redirect('members:main_menu_login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)    
            login(request, user)
            return redirect('LoginRegister:FTMainMenu')
    else:
        form = RegisterUserForm()
    
    return render(request, 'members/register_user.html', {
        'form':form,  
        })

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("familytracks:home")
        return render(request, 'members/update_user.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect("members:main_menu_login")