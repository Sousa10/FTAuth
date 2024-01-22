from django.db import models
from django.contrib.auth.models import AbstractUser, User

class PersonM(models.Model):
  LocationID = models.IntegerField(null=True)
  firstname = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255, null=True)
  MiddleName = models.CharField(max_length=255, null=True)
  Salutation = models.CharField(max_length=40, null=True)
  NameSuffix = models.CharField(max_length=120, null=True)
  Sex = models.CharField(max_length=40, null=True)
  EdDegree1 = models.CharField(max_length=40, null=True)
  EdMajor1 = models.CharField(max_length=80, null=True)
  EdDegree2 = models.CharField(max_length=40, null=True)
  EdMajor2 = models.CharField(max_length=80, null=True)
  DateJoinedTracker = models.DateField(auto_now_add=True)
  EmailPrimary = models.CharField(max_length=255, null=True)
  PostalCodePrimary = models.CharField(max_length=40, null=True)
  PhonePrimary = models.CharField(max_length=40, null=True)
  EmailSecondary = models.CharField(max_length=255, null=True)
  PostalCodeSecondary = models.CharField(max_length=40, null=True)
  PhoneSecondary = models.CharField(max_length=40, null=True)
  FTUserName = models.CharField(max_length=80, null=True)
  Password = models.CharField(max_length=255, null=True)
  
  class Meta:
        verbose_name_plural = 'Persons'
  def __str__(self):
     return self.firstname

class AcctRollupsM(models.Model):
  RollUpName = models.CharField(max_length=255, null=True)
  AcctType = models.CharField(max_length=80, null=True)

  class Meta:
        verbose_name_plural = 'Account Rollups'
  def __str__(self):
     return self.RollUpName

class AcctRollupsD(models.Model):
  RollUpName = models.CharField(max_length=255, null=True)
  AcctType = models.CharField(max_length=80, null=True)
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

  class Meta:
        verbose_name_plural = 'Account Detail Rollups'
  def __str__(self):
     return self.RollUpName

class SponRates(models.Model):
  Sequence = models.CharField(max_length=10, null=True)  
  Geography = models.CharField(max_length=120, null=True)
  Population = models.CharField(max_length=40, null=True)
  FTUserCount = models.CharField(max_length=40, null=True)
  Spots1_6Rate = models.CharField(max_length=40, null=True)
  Spot7Rate = models.CharField(max_length=40, null=True)

  def __str__(self):
      return self.Geography

class CalendarIncrements(models.Model):
  Sequence = models.IntegerField(null=True)
  FamilyID = models.IntegerField(null=True)
  PersonID = models.IntegerField(null=True)
  CalendarID = models.CharField(max_length=120, null=True)
  IncrementDate = models.DateField()
  IncrementTime = models.TimeField()

  def __str__(self):
      return self.Sequence

# 
# New 8/16 Start here, drop boxes for Calendar template
# 
class Calendars(models.Model):
   calendar = models.CharField(primary_key=True, max_length=40)
   name = models.CharField(max_length=64, blank=True, null=True)
   description = models.CharField(max_length=4000, blank=True, null=True)
   calendar_type = models.CharField(max_length=8, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'calendars'

   def __str__(self):
      return self.Calendar

class Views(models.Model):
   view = models.CharField(primary_key=True, max_length=20)
   name = models.CharField(max_length=64, blank=True, null=True)
   description = models.CharField(max_length=4000, blank=True, null=True)
   view_type = models.CharField(max_length=8, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'views'

   def __str__(self):
      return self.view

class Dates(models.Model):
   date = models.CharField(primary_key=True, max_length=20)
   name = models.CharField(max_length=64, blank=True, null=True)
   description = models.CharField(max_length=4000, blank=True, null=True)
   date_type = models.CharField(max_length=8, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'dates'

   def __str__(self):
      return self.date

class DefaultParams(models.Model):
    default_param_id = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendars, models.DO_NOTHING)
    view = models.ForeignKey('Views', models.DO_NOTHING)
    date = models.ForeignKey('Dates', models.DO_NOTHING, db_column='position_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_params'

    def __str__(self):
      return self.default_param_id
# 
#   KMS Start Day Picker
#
class Transactions(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class LinkClickCount(models.Model):
    link_name = models.CharField(max_length=100, unique=True)
    click_count = models.PositiveIntegerField(default=0)

    def increment(self):
        self.click_count += 1
        self.save()
