from django.urls import path
from . import views

app_name = 'familytracks'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('profiles_list/', views.profiles_list, name='profiles_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/follows/<int:pk>', views.follows, name='follows'),
    path('meep_like/<int:pk>', views.meep_like, name='meep_like'),
    path('meep_show/<int:pk>', views.meep_show, name='meep_show'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('delete_meep/<int:pk>', views.delete_meep, name="delete_meep"),
    path('edit_meep/<int:pk>', views.edit_meep, name="edit_meep"),
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user'),
]