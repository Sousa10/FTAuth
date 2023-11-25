from django.db import models

# Create your models here.

class CashInAcctM(models.Model):
  Status = models.CharField(max_length=10, null=True)
  AccountNumber = models.CharField(max_length=20, null=True)
  Description = models.CharField(max_length=255, null=True)
  Type = models.CharField(max_length=12, null=True)
  Statement = models.CharField(max_length=40, null=True) 
  Section = models.CharField(max_length=40, null=True) 
  Sequence = models.IntegerField(null=True)
  RollupType = models.CharField(max_length=60, null=True)

  class Meta:
        verbose_name_plural = 'Accounts'
  def __str__(self):
     return self.AccountNumber



class CashOutAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

  class Meta:
        verbose_name_plural = 'Expense Accounts'
  def __str__(self):
     return self.AccountNumber

class WhatWeOwnAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

  class Meta:
        verbose_name_plural = 'Asset Accounts'
  def __str__(self):
     return self.AccountNumber

class DebtsAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

  class Meta:
        verbose_name_plural = 'Liability Accounts'
  def __str__(self):
     return self.AccountNumber

class NetworthAcctM(models.Model):
  AccountNumber = models.CharField(max_length=40, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

  class Meta:
        verbose_name_plural = 'Equity Accounts'
  def __str__(self):
     return self.AccountNumber
  
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

class StatementRollups(models.Model):
  StatementType = models.CharField(max_length=10, null=True)
  Account = models.CharField(max_length=10, null=True)
  RollupName = models.CharField(max_length=80, null=True)

  class Meta:
        verbose_name_plural = 'Statement Rollups'
  def __str__(self):
     return self.RollupName

class StatementSections(models.Model):
  StatementType = models.CharField(max_length=10, null=True)
  Sequence = models.IntegerField(null=True)
  LineName = models.CharField(max_length=40, null=True)

  class Meta:
        verbose_name_plural = 'Statement Sections'
  def __str__(self):
     return self.LineName

