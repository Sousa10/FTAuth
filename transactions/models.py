from django.db import models

# Create your models here.

class CashInAcctM(models.Model):
  AccountNumber = models.CharField(max_length=20, null=True)
  Description = models.CharField(max_length=255, null=True)
  DrCrBal = models.CharField(max_length=20, null=True)

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
