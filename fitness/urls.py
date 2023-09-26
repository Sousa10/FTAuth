from django.urls import path
from . import views

urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphen - and _ underscore stuff
    # UUID: universally unique identifier

    # path('venue_text/', views.venue_text, name='venue_text'),
    # path('venue_csv/', views.venue_csv, name='venue_csv'),
    # path('venue_pdf/', views.venue_pdf, name='venue_pdf'),
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
]