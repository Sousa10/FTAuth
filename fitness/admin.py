from django.contrib import admin
from .models import workout, training_routine
from .models import ExcerciseList
from .models import golf_course

# Register your models here.
admin.site.register(workout)
admin.site.register(training_routine)
admin.site.register(ExcerciseList)
admin.site.register(golf_course)
