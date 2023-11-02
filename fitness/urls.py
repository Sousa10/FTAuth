from django.urls import path
from . import views

app_name = 'fitness'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('', views.tutorial, name="tutorial"),
    path('app_tutorial/', views.tutorial, name='tutorial2'),
    path('upperbodygymworkouts/', views.UpperBodyGymWorkouts, name='UpperBodyGymWorkouts'),
    path('upperbodyhomeworkouts/', views.UpperBodyHomeWorkouts, name='UpperBodyHomeWorkouts'),
    path('training_routines', views.training_routines, name='training_routines'),
    path('search_workouts', views.search_workouts, name='search_workouts' ),
    path('show_workout/<int:workout_id>', views.show_workout, name='show_workout'),
    path('show_excercise/<int:excercise_id>', views.show_excercise, name='show_excercise'),
    path('show_routine/<int:routine_id>', views.show_routine, name='show_routine'),
    path('show_construction', views.show_construction, name='show_construction'),
    path('workouts', views.workouts, name='workouts'),
    path('excercises', views.excercises, name='excercises'),
    path('golf_courses', views.golf_courses, name='golf_courses'),
    path('addworkout', views.AddWorkout, name='AddWorkout'),
    path('addexcercise', views.AddExcercise, name='AddExcercise'),
    path('addroutine', views.AddRoutine, name='AddRoutine'),
    ]                                      