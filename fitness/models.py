from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class AppTutorial(models.Model):
    video = EmbedVideoField(blank=True) # an empty field is fine for me

class ExcerciseList(models.Model):
  Reference = models.CharField(max_length=80, null=True)
  Region = models.CharField(max_length=80, null=True)
  Area = models.CharField(max_length=80, null=True)
  Exercise = models.CharField(max_length=80, null=True)
  Description = models.CharField(max_length=3000, null=True)
  Instructions = models.CharField(max_length=3000, null=True)

  class Meta:
        verbose_name_plural = 'Excercises'
  def __str__(self):
     return self.Exercise
  
class WorkoutHeader(models.Model):
  WorkoutID = models.IntegerField(null=True)
  WorkoutType = models.CharField(max_length=80, null=True)
  WorkoutName = models.CharField(max_length=1000, null=True)
  Description = models.CharField(max_length=3000, null=True)
  Frequency = models.CharField(max_length=220, null=True)
  Level = models.CharField(max_length=80, null=True)
  Description = models.CharField(max_length=3000, null=True)
  Instructions = models.CharField(max_length=3000, null=True)
  
  class Meta:
        verbose_name_plural = 'Workout Name'
  def __str__(self):
     return self.WorkoutID

class workout(models.Model):
  WorkoutName = models.CharField(max_length=220, null=True)
  ExcerID = models.IntegerField(null=True)
  Region = models.CharField(max_length=80, null=True)
  Area = models.CharField(max_length=80, null=True)
  Exercise = models.CharField(max_length=80, null=True)
  SetOneReps = models.IntegerField(null=True)
  SetOneWeight = models.CharField(max_length=80, null=True)
  SetTwoReps = models.IntegerField(null=True)
  SetTwoWeight = models.CharField(max_length=80, null=True)
  SetThreeReps = models.IntegerField(null=True)
  SetThreeWeight = models.CharField(max_length=80, null=True)
  SetFourReps = models.IntegerField(null=True)
  SetFourWeight = models.CharField(max_length=80, null=True)

  class Meta:
        verbose_name_plural = 'Workout Excercise'
  def __str__(self):
    return self.WorkoutName
  
class training_routine(models.Model):
  RoutineName = models.CharField(max_length=120, null=True)
  Description = models.CharField(max_length=1000, null=True)
  Benefits = models.CharField(max_length=1000, null=True)
  Instructions = models.CharField(max_length=1000, null=True)
  ResultsComments = models.CharField(max_length=1000, null=True)

  class Meta:
        verbose_name_plural = 'Training Routine'
  def __str__(self):
    return self.RoutineName