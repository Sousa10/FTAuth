from django.contrib import admin
from .models import Venue
from .models import Event
from .models import TrackerUser

# Register your models here.
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(TrackerUser)