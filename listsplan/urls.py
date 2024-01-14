from django.urls import path
from . import views

app_name = 'listsplan'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('FTListChores/', views.FTListChores, name='FTListChores'),
    path('FTListChores/<int:listheader_id>/', views.FTListChores, name='FTListChores_with_id'),
    path('listHeader/delete/<int:pk>/', views.listHeader_delete, name='listHeader_delete'),
    path('listDetail/delete/<int:pk>/', views.listDetail_delete, name='listDetail_delete'),
    path('listHeader_update/update/<int:pk>/', views.listHeader_update, name='listHeader_update'),
    path('listDetail_update/update/<int:pk>/', views.listDetail_update, name='listDetail_update'),
]