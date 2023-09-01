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

class CashInAcctM(models.Model):
  AccountNumber = models.CharField(max_length=20, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class CashOutAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class WhatWeOwnAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class DebtsAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class NetworthAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class AcctRollupsM(models.Model):
  RollUpName = models.CharField(max_length=255, null=True)
  AcctType = models.CharField(max_length=80, null=True)

class AcctRollupsD(models.Model):
  RollUpName = models.CharField(max_length=255, null=True)
  AcctType = models.CharField(max_length=80, null=True)
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

class TransBatch(models.Model):
  TransBatchName = models.CharField(max_length=120, null=True)
  TransBatchDate = models.DateField()
  Created = models.DateTimeField(auto_now_add=True)
  LastUpdated = models.DateTimeField(auto_now=True) 

class TransHeader(models.Model):
  TransBatchID = models.ForeignKey('TransBatch', on_delete=models.CASCADE)
  TransDescription = models.CharField(max_length=120, null=True)
  TransDate = models.DateField()
  TransNote = models.CharField(max_length=240, null=True)
  Created = models.DateTimeField(auto_now_add=True)
  LastUpdated = models.DateTimeField(auto_now=True) 

class TransDetail(models.Model):
  TransHeaderID = models.ForeignKey('TransHeader', on_delete=models.CASCADE)
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrAmount = models.IntegerField()
  CrAmount = models.IntegerField()
  Created = models.DateTimeField(auto_now_add=True)
  LastUpdated = models.DateTimeField(auto_now=True) 

class ListHeaderT(models.Model):
    PersonFK = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    LHName = models.CharField(max_length=240)
    LHDescription = models.CharField(max_length=240)

    def __str__(self):
        return self.LHName

class ListDetailsT(models.Model):
    ListHeaderFK = models.ForeignKey('ListHeaderT', on_delete=models.CASCADE)
    ListDetailFK = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='predecessor')
    LNNumber = models.IntegerField()
    LHName = models.CharField(max_length=240)

    def __str__(self):
        return self.LHName

class SponRates(models.Model):
  Sequence = models.CharField(max_length=10, null=True)  
  Geography = models.CharField(max_length=120, null=True)
  Population = models.CharField(max_length=40, null=True)
  FTUserCount = models.CharField(max_length=40, null=True)
  Spots1_6Rate = models.CharField(max_length=40, null=True)
  Spot7Rate = models.CharField(max_length=40, null=True)

class CalendarIncrements(models.Model):
  Sequence = models.IntegerField(null=True)
  FamilyID = models.IntegerField(null=True)
  PersonID = models.IntegerField(null=True)
  CalendarID = models.CharField(max_length=120, null=True)
  IncrementDate = models.DateField()
  IncrementTime = models.TimeField()

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

class Views(models.Model):
   view = models.CharField(primary_key=True, max_length=20)
   name = models.CharField(max_length=64, blank=True, null=True)
   description = models.CharField(max_length=4000, blank=True, null=True)
   view_type = models.CharField(max_length=8, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'views'

class Dates(models.Model):
   date = models.CharField(primary_key=True, max_length=20)
   name = models.CharField(max_length=64, blank=True, null=True)
   description = models.CharField(max_length=4000, blank=True, null=True)
   date_type = models.CharField(max_length=8, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'dates'

class DefaultParams(models.Model):
    default_param_id = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendars, models.DO_NOTHING)
    view = models.ForeignKey('Views', models.DO_NOTHING)
    date = models.ForeignKey('Dates', models.DO_NOTHING, db_column='position_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_params'
# 
#   KMS Start Day Picker
#
class Transactions(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description