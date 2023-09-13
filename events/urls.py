from django.urls import path
from . import views

urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphen - and _ underscore stuff
    # UUID: universally unique identifier

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events_list/', views.events_list, name='events-list'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('search_venues/', views.search_venues, name='search-venues'),
    path('show_venues/', views.show_venues, name='show-venues'),
    path('venue/<int:venue_id>', views.venuex, name='show-venue'),
    path('venue/', views.venuex, name='show-venue-no-id'),
    path('update_venue/<int:venue_id>', views.update_venue, name='update-venue'),
    path('add_event/', views.add_event, name='add-event'),
    path('update_event/<int:event_id>', views.update_event, name='update-event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete-event'),
    path('delete_venu/<int:venue_id>', views.delete_venue, name='delete-venue'),
    path('venue_text/', views.venue_text, name='venue_text'),
    path('venue_csv/', views.venue_csv, name='venue_csv'),
    path('venue_pdf/', views.venue_pdf, name='venue_pdf'),
]