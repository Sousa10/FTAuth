from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'LoginRegister'

urlpatterns = [
    path('LoginRegister/', views.LoginRegister, name='LoginRegister'),
    path('LoginRegister/FTMainMenu/', views.FTMainMenu, name='FTMainMenu'),
    path('LoginRegister/FTFinances/', views.FTFinances, name='FTFinances'),
    path('LoginRegister/FTCalendar/', views.FTCalendar, name='FTCalendar'),
    path('LoginRegister/FTToDos/', views.FTToDos, name='FTToDos'),
    path('LoginRegister/FTListChores/', views.FTListChores, name='FTListChores'),
    path('LoginRegister/FTFamilyTracks/', views.FTFamilyTracks, name='FTFamilyTracks'),
    path('LoginRegister/FTFitnessSports/', views.FTFitnessSports, name='FTFitnessSports'),
    path('LoginRegister/FTGrocery/', views.FTGrocery, name='FTGrocery'),
    path('LoginRegister/FTAcministration/', views.FTAcministration, name='FTAcministration'),
    path('LoginRegister/login/', auth_views.LoginView.as_view(template_name='FTperson_login.html', authentication_form=LoginForm), name='login'),
]