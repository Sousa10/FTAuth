from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm, ProfilePicForm
from django.contrib.auth.models import User

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
        # profiles = Profile.objects.exclude(user=request.user)
        profiles = Profile.objects.all()
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
    
def meep_like(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if meep.likes.filter(id=request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("You Must Be Logged In to View This Page"))
        return redirect('familytracks:main_landing_page')

def meep_show(request, pk):
    meep = get_object_or_404(Meep, id=pk)
    if meep:
        return render(request, "familytracks/show_meep.html", {"meep":meep})
    else:
        messages.success(request, ("That meep doesn't exist"))
        return redirect('familytracks:main_landing_page')

def unfollow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.remove(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Unfollowed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('familytracks:main_landing_page')

def follow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.add(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Followed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('familytracks:main_landing_page')
     
def followers(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'familytracks/followers.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('familytracks:main_landing_page')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('familytracks:main_landing_page')
     
def follows(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'familytracks/follows.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('familytracks:main_landing_page')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('familytracks:main_landing_page')
      
def delete_meep(request, pk):
	if request.user.is_authenticated:
		meep = get_object_or_404(Meep, id=pk)
		# Check to see if you own the meep
		if request.user.username == meep.user.username:
			# Delete The Meep
			meep.delete()
			
			messages.success(request, ("The Meep Has Been Deleted!"))
			return redirect(request.META.get("HTTP_REFERER"))	
		else:
			messages.success(request, ("You Don't Own That Meep!!"))
			return redirect('familytracks:main_landing_page')

	else:
		messages.success(request, ("Please Log In To Continue..."))
		return redirect(request.META.get("HTTP_REFERER"))

def edit_meep(request,pk):
	if request.user.is_authenticated:
		# Grab The Meep!
		meep = get_object_or_404(Meep, id=pk)

		# Check to see if you own the meep
		if request.user.username == meep.user.username:
			
			form = MeepForm(request.POST or None, instance=meep)
			if request.method == "POST":
				if form.is_valid():
					meep = form.save(commit=False)
					meep.user = request.user
					meep.save()
					messages.success(request, ("Your Meep Has Been Updated!"))
					return redirect(request.META.get("HTTP_REFERER"))
			else:
				return render(request, "familytracks/edit_meep.html", {'form':form, 'meep':meep})
	
		else:
			messages.success(request, ("You Don't Own That Meep!!"))
			return redirect('familytracks:main_landing_page')

	else:
		messages.success(request, ("Please Log In To Continue..."))
		return redirect('familytracks:main_landing_page')
	
def search(request):
	if request.method == "POST":
		# Grab the form field input
		search = request.POST['search']
		# Search the database
		searched = Meep.objects.filter(body__contains = search)

		return render(request, 'familytracks/search.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'familytracks/search.html', {})

def search_user(request):
	if request.method == "POST":
		# Grab the form field input
		search = request.POST['search']
		# Search the database
		searched = User.objects.filter(username__contains = search)

		return render(request, 'familytracks/search_user.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'familytracks/search_user.html', {})