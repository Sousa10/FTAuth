from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('', views.members, name='members'),
    path('main_menu_login/', views.main_menu_login, name='main_menu_login'),
    path('register_user', views.register_user, name='register_user' )
]