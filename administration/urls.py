from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('show_construction', views.show_construction, name='show_construction'),
]