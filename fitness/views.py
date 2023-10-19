from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect 
import csv
import io
from .models import workout, training_routine
from .forms import WorkoutForm

def home(request):
    return render(request, 'fitness/main_landing_page.html', {})

def main_landing_page(request):
    return render(request, 'fitness/main_landing_page.html', {})

def tutorial(request):
    return render(request, 'fitness/app_tutorial.html', {})

def UpperBodyGymWorkouts(request):
    return render(request, 'fitness/UpperBodyGymWorkouts.html', {})

def UpperBodyHomeWorkouts(request):
    return render(request, 'fitness/UpperBodyHomeWorkouts.html', {})

def AddWorkout(request):
    submitted = False
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('addworkout?submitted=True')   
    else:
        form = WorkoutForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'fitness/AddWorkout.html', {'form':form, 'submitted':submitted})

def show_workout(request, workout_id):
    workout_info = workout.objects.get(pk=workout_id)
    return render(request, 'fitness/show_workout.html', {'workout': workout_info})

def workouts(request):
    workout_list = workout.objects.all()
    return render(request, 'fitness/workouts.html', {'workout_list': workout_list})

def training_routines(request):
    routine_list = training_routine.objects.all()
    return render(request, 'fitness/training_routines.html', {'routine_list': routine_list})

def search_workouts(request):
    return render(request, 'fitness.search_workouts.html', {})
