from django.shortcuts import render, redirect
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm, ProfilePicForm

def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, ("Your Meep has been posted"))
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'familytracks/home.html', {"meeps":meeps, "form": form})
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'familytracks/home.html', {"meeps":meeps})

def main_landing_page(request):
    return render(request, 'familytracks/main_landing_page.html', {})

def profiles_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'familytracks/profiles_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("You Must Be Logged In to View This Page"))
        return redirect('familytracks:main_landing_page')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user_id=pk).order_by("-created_at")

        # Post Form logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            # save the profile
            current_user_profile.save()
        return render(request, "familytracks/profile.html", {"profile": profile, "meeps":meeps})
    else:
        messages.success(request, ("You Must Be Logged In to View This Page"))
        return redirect('familytracks:main_landing_page')