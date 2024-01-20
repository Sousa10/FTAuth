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

    def __str__(self):
        return self.SLAccount

# ################################################# 
#     NEW STARTING 1/13   
###################################################
class StatementSections(models.Model):	
    SSPersonFK = models.ForeignKey(PersonM, null=True, on_delete=models.CASCADE)	
    SSName = models.CharField(max_length=240, default='')	
    SSDescription = models.CharField(max_length=960, default='')	
    SSIncomeStatementYN = models.CharField(max_length=3, default='') 	
    SSIncomeStatementSequence = models.CharField(max_length=3, default='') 	
    SSBalanceSheetStatementYN = models.CharField(max_length=3, default='')	
    SSBalanceSheetStatementSequence = models.CharField(max_length=3, default='')	
    SSCashFlowStatementYN = models.CharField(max_length=3, default='')	
    SSCashFlowStatementSequence = models.CharField(max_length=3, default='')	
    SSExpenseStatementYN = models.CharField(max_length=3, default='')	
    SSExpenseStatementSequence = models.CharField(max_length=3, default='')	
    SSBudgetStatementYN = models.CharField(max_length=3, default='')	
    SSBudgetStatementSequence = models.CharField(max_length=3, default='')	
	
    def __str__(self):	
        return self.SSName
    
class StatementLinesLine(models.Model):		
    SLStatementSectionFK = models.ForeignKey('StatementSections', null=True, blank=True, on_delete=models.CASCADE)		
    SLStatementLineFK = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='predecessor')		
    SLName = models.CharField(max_length=240)		
    SLDescription = models.CharField(max_length=240)		
    SLIncomeStatement = models.CharField(max_length=3, null=True) 		
    SLIncomeStatementSection = models.CharField(max_length=80, null=True) 		
    SLIncomeStatementSequence = models.IntegerField(null=True) 		
    SLBalanceSheetStatement = models.CharField(max_length=3, null=True) 		
    SLBalanceSheetStatementSection = models.CharField(max_length=80, null=True) 		
    SLBalanceSheetStatementSequence = models.IntegerField(null=True) 		
    SLCashFlowStatement = models.CharField(max_length=3, null=True)		
    SLCashFlowStatementSection = models.CharField(max_length=80, null=True) 		
    SLCashFlowStatementSequence = models.IntegerField(null=True) 		
    SLExpenseStatement = models.CharField(max_length=3, null=True) 		
    SLExpenseStatementSection = models.CharField(max_length=80, null=True) 		
    SLExpenseStatementSequence = models.IntegerField(null=True) 		
    SLBudgetStatement = models.CharField(max_length=3, null=True) 		
    SLBudgetStatementSection = models.CharField(max_length=80, null=True) 		
    SLBudgetStatementSequence = models.IntegerField(null=True) 		
		
    def __str__(self):		
        return self.SLName

class StatementLineAccounts(models.Model):		
    SLAStatementSectionFK = models.ForeignKey('StatementSections', null=True, blank=True, on_delete=models.CASCADE)		
    SLAStatementLineFK = models.ForeignKey('StatementLinesLine', null=True, blank=True, on_delete=models.CASCADE)		
    SLAStatementAccountFK = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='predecessor')		
    SAAccount = models.IntegerField()		
    SLAAccountType = models.CharField(max_length=12)		
    SLADescription = models.CharField(max_length=240)		
		
    def __str__(self):		
        return self.SAAccount		



