from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
]