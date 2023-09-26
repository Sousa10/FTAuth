from django.contrib import admin
from .models import Venue
from .models import Event
from .models import TrackerUser
# KMS New Calendar Start
from .models import EventC
# KMS New Calendar End

# Register your models here.
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(TrackerUser)
# KMS New Calendar Start
admin.site.register(EventC)
# KMS New Calendar End