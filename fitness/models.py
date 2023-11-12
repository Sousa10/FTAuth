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
  
class golf_course(models.Model):
  Course = models.CharField(max_length=120, null=True)
  CoursePar = models.CharField(max_length=12, null=True)
  Yards = models.CharField(max_length=12, null=True)
  Slope = models.CharField(max_length=12, null=True)
  Rating = models.CharField(max_length=12, null=True)
  Description = models.CharField(max_length=1000, null=True)
  Hole1Par = models.CharField(max_length=12, null=True)
  Hole1Yardage = models.CharField(max_length=12, null=True)
  Hole1Handicap = models.CharField(max_length=12, null=True)
  Hole2Par = models.CharField(max_length=12, null=True)
  Hole2Yardage = models.CharField(max_length=12, null=True)
  Hole2Handicap = models.CharField(max_length=12, null=True)
  Hole3Par = models.CharField(max_length=12, null=True)
  Hole3Yardage = models.CharField(max_length=12, null=True)
  Hole3Handicap = models.CharField(max_length=12, null=True)
  Hole4Par = models.CharField(max_length=12, null=True)
  Hole4Yardage = models.CharField(max_length=12, null=True)
  Hole4Handicap = models.CharField(max_length=12, null=True)
  Hole5Par = models.CharField(max_length=12, null=True)
  Hole5Yardage = models.CharField(max_length=12, null=True)
  Hole5Handicap = models.CharField(max_length=12, null=True)
  Hole6Par = models.CharField(max_length=12, null=True)
  Hole6Yardage = models.CharField(max_length=12, null=True)
  Hole6Handicap = models.CharField(max_length=12, null=True)
  Hole7Par = models.CharField(max_length=12, null=True)
  Hole7Yardage = models.CharField(max_length=12, null=True)
  Hole7Handicap = models.CharField(max_length=12, null=True)
  Hole8Par = models.CharField(max_length=12, null=True)
  Hole8Yardage = models.CharField(max_length=12, null=True)
  Hole8Handicap = models.CharField(max_length=12, null=True)
  Hole9Par = models.CharField(max_length=12, null=True)
  Hole9Yardage = models.CharField(max_length=12, null=True)
  Hole9Handicap = models.CharField(max_length=12, null=True)
  Hole10Par = models.CharField(max_length=12, null=True)
  Hole10Yardage = models.CharField(max_length=12, null=True)
  Hole10Handicap = models.CharField(max_length=12, null=True)
  Hole11Par = models.CharField(max_length=12, null=True)
  Hole11Yardage = models.CharField(max_length=12, null=True)
  Hole11Handicap = models.CharField(max_length=12, null=True)
  Hole12Par = models.CharField(max_length=12, null=True)
  Hole12Yardage = models.CharField(max_length=12, null=True)
  Hole12Handicap = models.CharField(max_length=12, null=True)
  Hole13Par = models.CharField(max_length=12, null=True)
  Hole13Yardage = models.CharField(max_length=12, null=True)
  Hole13Handicap = models.CharField(max_length=12, null=True)
  Hole14Par = models.CharField(max_length=12, null=True)
  Hole14Yardage = models.CharField(max_length=12, null=True)
  Hole14Handicap = models.CharField(max_length=12, null=True)
  Hole15Par = models.CharField(max_length=12, null=True)
  Hole15Yardage = models.CharField(max_length=12, null=True)
  Hole15Handicap = models.CharField(max_length=12, null=True)
  Hole16Par = models.CharField(max_length=12, null=True)
  Hole16Yardage = models.CharField(max_length=12, null=True)
  Hole16Handicap = models.CharField(max_length=12, null=True)
  Hole17Par = models.CharField(max_length=12, null=True)
  Hole17Yardage = models.CharField(max_length=12, null=True)
  Hole17Handicap = models.CharField(max_length=12, null=True)
  Hole18Par = models.CharField(max_length=12, null=True)
  Hole18Yardage = models.CharField(max_length=12, null=True)
  Hole18Handicap = models.CharField(max_length=12, null=True)
  
  class Meta:
        verbose_name_plural = 'Golf Course'
  def __str__(self):
    return self.Course
  
class golf_score(models.Model):
  GolfCourse = models.CharField(max_length=120, null=True)
  Score = models.CharField(max_length=20, null=True)
  Date = models.CharField(max_length=20, null=True)
  Player2 = models.CharField(max_length=60, null=True)
  Player3 = models.CharField(max_length=60, null=True)
  Player4 = models.CharField(max_length=60, null=True)
  Hole1Par = models.CharField(max_length=12, null=True)
  Hole1Score = models.CharField(max_length=12, null=True)
  Hole2Par = models.CharField(max_length=12, null=True)
  Hole2Score = models.CharField(max_length=12, null=True)
  Hole3Par = models.CharField(max_length=12, null=True)
  Hole3Score = models.CharField(max_length=12, null=True)
  Hole4Par = models.CharField(max_length=12, null=True)
  Hole4Score = models.CharField(max_length=12, null=True)
  Hole5Par = models.CharField(max_length=12, null=True)
  Hole5Score = models.CharField(max_length=12, null=True)
  Hole6Par = models.CharField(max_length=12, null=True)
  Hole6Score = models.CharField(max_length=12, null=True)
  Hole7Par = models.CharField(max_length=12, null=True)
  Hole7Score = models.CharField(max_length=12, null=True)
  Hole8Par = models.CharField(max_length=12, null=True)
  Hole8Score = models.CharField(max_length=12, null=True)
  Hole9Par = models.CharField(max_length=12, null=True)
  Hole9Score = models.CharField(max_length=12, null=True)
  Hole10Par = models.CharField(max_length=12, null=True)
  Hole10Score = models.CharField(max_length=12, null=True)
  Hole11Par = models.CharField(max_length=12, null=True)
  Hole11Score = models.CharField(max_length=12, null=True)
  Hole12Par = models.CharField(max_length=12, null=True)
  Hole12Score = models.CharField(max_length=12, null=True)
  Hole13Par = models.CharField(max_length=12, null=True)
  Hole13Score = models.CharField(max_length=12, null=True)
  Hole14Par = models.CharField(max_length=12, null=True)
  Hole14Score = models.CharField(max_length=12, null=True)
  Hole15Par = models.CharField(max_length=12, null=True)
  Hole15Score = models.CharField(max_length=12, null=True)
  Hole16Par = models.CharField(max_length=12, null=True)
  Hole16Score = models.CharField(max_length=12, null=True)
  Hole17Par = models.CharField(max_length=12, null=True)
  Hole17Score = models.CharField(max_length=12, null=True)
  Hole18Par = models.CharField(max_length=12, null=True)
  Hole18Score = models.CharField(max_length=12, null=True)
  Comments = models.CharField(max_length=2000, null=True)

  class Meta:
        verbose_name_plural = 'Golf Score'
  def __str__(self):
    return self.Score