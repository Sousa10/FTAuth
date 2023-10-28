from django.contrib import admin
from .models import workout, training_routine
from .models import ExcerciseList

# Register your models here.
admin.site.register(workout)
admin.site.register(training_routine)
admin.site.register(ExcerciseList)
