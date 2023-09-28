from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class AppTutorial(models.Model):
    video = EmbedVideoField(blank=True) # an empty field is fine for me
    