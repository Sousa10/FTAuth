from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv
import io
from .models import workout, training_routine, ExcerciseList, golf_course
from .models import *
from .forms import WorkoutForm
from .forms import ExcerciseForm
from .forms import RoutineForm
from .forms import GolfCourseForm
from .forms import GolfScoreForm
from django.views import generic
from django.core.paginator import Paginator
from django.http import JsonResponse
from LoginRegister.utils import increment_click_count

def home(request):
    return render(request, 'fitness/main_landing_page.html', {})

def main_landing_page(request):
    click_count = increment_click_count('fitness')
    return render(request, 'fitness/main_landing_page.html', {'click_count': click_count,})

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

def AddExcercise(request):
    submitted = False
    if request.method == "POST":
        form = ExcerciseForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('addexcercise?submitted=True')   
    else:
        form = ExcerciseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'fitness/AddExcercise.html', {'form':form, 'submitted':submitted})

def AddRoutine(request):
    submitted = False
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('addroutine?submitted=True')   
    else:
        form = RoutineForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'fitness/AddRoutine.html', {'form':form, 'submitted':submitted})

def AddGolfCourse(request):
    yardage_fields = [f'Hole{i}Yardage' for i in range(1, 19)]
    handicap_fields = [f'Hole{i}Handicap' for i in range(1, 19)]
    submitted = False
    if request.method == "POST":
        form = GolfCourseForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('addgolfcourse?submitted=True')   
    else:
        form = GolfCourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'fitness/AddGolfCourse.html', {'form':form, 'submitted':submitted,  'yardage_fields': yardage_fields,
        'handicap_fields': handicap_fields,})

def training_routines(request):
    routine_list = training_routine.objects.all()

    # Set up Pagination
    p = Paginator(training_routine.objects.all(), 8)
    page = request.GET.get('page')
    routine_p = p.get_page(page)
    nums = "x" * routine_p.paginator.num_pages
    return render(request, 'fitness/training_routines.html', {
        'routine_list': routine_list,
        'routine_p': routine_p,
        'nums' :nums
        })

def search_workouts(request):
    if request.method == "POST":
        searched = request.POST['searched']   
        workouts = workout.objects.filter(WorkoutName__contains=searched)
        return render(request, 'fitness/search_workouts.html', {'searched':searched, 'workouts':workouts})
    else:
        return render(request, 'fitness/search_workouts.html', {})


def workouts(request):
    workout_list = workout.objects.all()
    return render(request, 'fitness/workouts.html', {'workout_list': workout_list})

def show_workout(request, workout_id):
    workout_info = workout.objects.get(pk=workout_id)
    return render(request, 'fitness/show_workout.html', {'workout': workout_info})

def show_excercise(request, excercise_id):
    excercise_info = ExcerciseList.objects.get(pk=excercise_id)
    return render(request, 'fitness/show_excercise.html', {'excercise': excercise_info})

def show_golf_course(request, golf_course_id):
    course_info = golf_course.objects.get(pk=golf_course_id)

    # Extract relevant data from the course_info
    data = {
        'Hole1Par': course_info.Hole1Par,
        'Hole2Par': course_info.Hole2Par,
        'Hole3Par': course_info.Hole3Par,
        'Hole4Par': course_info.Hole4Par,
        'Hole5Par': course_info.Hole5Par,
        'Hole6Par': course_info.Hole6Par,
        'Hole7Par': course_info.Hole7Par,
        'Hole8Par': course_info.Hole8Par,
        'Hole9Par': course_info.Hole9Par,
        'Hole10Par': course_info.Hole10Par,
        'Hole11Par': course_info.Hole11Par,
        'Hole12Par': course_info.Hole12Par,
        'Hole13Par': course_info.Hole13Par,
        'Hole14Par': course_info.Hole14Par,
        'Hole15Par': course_info.Hole15Par,
        'Hole16Par': course_info.Hole16Par,
        'Hole17Par': course_info.Hole17Par,
        'Hole18Par': course_info.Hole18Par,
        # Add other fields here
    }

    # If it's an AJAX request, return JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(data)
    return render(request, 'fitness/show_golf_course.html', {'golf_course': course_info})

def show_golf_round(request, golf_round_id):
    round_info = golf_score.objects.get(pk=golf_round_id)

    # Extract relevant data from the course_info
    data = {
        'Hole1Par': round_info.Hole1Par,
        'Hole2Par': round_info.Hole2Par,
        'Hole3Par': round_info.Hole3Par,
        'Hole4Par': round_info.Hole4Par,
        'Hole5Par': round_info.Hole5Par,
        'Hole6Par': round_info.Hole6Par,
        'Hole7Par': round_info.Hole7Par,
        'Hole8Par': round_info.Hole8Par,
        'Hole9Par': round_info.Hole9Par,
        'Hole10Par': round_info.Hole10Par,
        'Hole11Par': round_info.Hole11Par,
        'Hole12Par': round_info.Hole12Par,
        'Hole13Par': round_info.Hole13Par,
        'Hole14Par': round_info.Hole14Par,
        'Hole15Par': round_info.Hole15Par,
        'Hole16Par': round_info.Hole16Par,
        'Hole17Par': round_info.Hole17Par,
        'Hole18Par': round_info.Hole18Par,
        # Add other fields here
    }

    # If it's an AJAX request, return JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(data)
    return render(request, 'fitness/show_golf_round.html', {'round_info': round_info})

def show_routine(request, routine_id):
    routine_info = training_routine.objects.get(pk=routine_id)
    return render(request, 'fitness/show_routine.html', {'routine': routine_info})

def show_construction(request):
    return render(request, 'fitness/show_construction.html', {})

def excercises(request):
    excercise_list = ExcerciseList.objects.all()

    # Set up Pagination
    p = Paginator(ExcerciseList.objects.all(), 11)
    page = request.GET.get('page')
    excer_p = p.get_page(page)
    nums = "x" * excer_p.paginator.num_pages

    if request.method == 'POST':
        form = ExcerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitness:excercises')
    else:
        exerciseForm = ExcerciseForm()
        # print(exerciseForm)

    return render(request, 'fitness/excercises.html', {
        'exerciseForm': exerciseForm,
        'excercise_list': excercise_list,
        'excer_p':excer_p,
        'nums':nums
        })

def exercise_update(request, pk):
    exercice = get_object_or_404(ExcerciseList, pk=pk)
    if request.method == 'POST':
        form = ExcerciseForm(request.POST, instance=exercice)
        if form.is_valid():
            form.save()
            return redirect('fitness:excercises')
    else:
        form = ExcerciseForm(instance=exercice)
    return render(request, 'fitness/excercises.html', {
        'form': form,
        'exercice': exercice,
        'title': 'Edit Cash In Account',
    })

def golf_courses(request):
    course_list = golf_course.objects.all()

    # Set up Pagination
    p = Paginator(golf_course.objects.all(), 8)
    page = request.GET.get('page')
    course_p = p.get_page(page)
    nums = "x" * course_p.paginator.num_pages
    return render(request, 'fitness/golf_courses.html', {
        'course_list':course_list,
        'course_p':course_p,
        'nums':nums
        })
 
def AddGolfScore(request):
    score_fields = [f'Hole{i}Score' for i in range(1, 19)]
    submitted = False
    if request.method == "POST":
        form = GolfScoreForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('addgolfscore?submitted=True')   
    else:
        form = GolfScoreForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'fitness/golf_score.html', {'form':form, 'submitted':submitted, 'score_fields': score_fields})

def golf_rounds(request):
    round_list = golf_score.objects.all()

    # Set up Pagination
    p = Paginator(golf_score.objects.all(), 8)
    page = request.GET.get('page')
    round_p = p.get_page(page)
    nums = "x" * round_p.paginator.num_pages
    return render(request, 'fitness/golf_rounds.html', {
        'round_list':round_list,
        'round_p':round_p,
        'nums':nums
        })

def exercise_delete(request, pk):
    exercise = get_object_or_404(ExcerciseList, pk=pk)
    exercise.delete()

    return redirect('fitness:excercises')