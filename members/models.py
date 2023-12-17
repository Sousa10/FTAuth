from django.db import models
from django.contrib.auth.models import AbstractUser, User

# class CustomUser(AbstractUser):
#     password_changed = models.BooleanField(default=False)

# CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
# CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'