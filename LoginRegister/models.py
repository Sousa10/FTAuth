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

class TransactionsT(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCr = models.CharField(max_length=20, null=True)
  Amount = models.IntegerField
  Created = models.DateField
  LastUpdated = models.DateField  

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
    LHDescription = models.CharField(max_length=480)

    def __str__(self):
        return self.LHName
