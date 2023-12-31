from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_menu_login/', views.main_menu_login, name='main_menu_login'),
    path('register_user', views.register_user, name='register_user' ),
    path('update_user', views.update_user, name='update_user' ),
    path('logout_user', views.logout_user, name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]