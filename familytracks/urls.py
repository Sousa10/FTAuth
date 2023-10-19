from django.urls import path
from . import views

app_name = 'familytracks'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('profiles_list/', views.profiles_list, name='profiles_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
]