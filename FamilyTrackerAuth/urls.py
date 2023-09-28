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
    path('familytracks/', include('familytracks.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
