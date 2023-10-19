from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(Profile)

#Mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Meep)