from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home, name="home"),
    # path('', views.members, name='members'),
    path('main_menu_login/', views.main_menu_login, name='main_menu_login'),
    path('register_user', views.register_user, name='register_user' ),
    path('logout_user', views.logout_user, name='logout'),
]