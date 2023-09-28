from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('', views.tutorial, name="tutorial"),
    path('app_tutorial/', views.tutorial, name='tutorial2'),
]