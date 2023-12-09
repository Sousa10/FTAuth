from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('LoginRegister.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('fitness/', include('fitness.urls')),
    path('calendar10', include('calendar10.urls')),
    path('transactions/', include('transactions.urls')),
    path('familytracks/', include('familytracks.urls')),
    path('cal/', include('cal.urls')),
    path('administration/', include('administration.urls')),
    path('listsplan/', include('listsplan.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)