from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # path('event/', views.event, name='event_new'),
]