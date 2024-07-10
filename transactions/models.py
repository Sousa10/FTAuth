from django.db import models
from django.conf import settings

# #################################################
#     NEW STARTING 1/21
###################################################

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PersonM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


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

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<< Financial Statements >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class FinStatements(models.Model):
    FSPersonFK = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    FSName = models.CharField(max_length=240, default='')
    FSCurrentDate = models.DateField(auto_now_add=True)
    FSFromDate = models.DateField()
    FSThroughDate = models.DateField()
    FSPostedDate = models.DateField()

    def __str__(self):
        return self.FSName

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< Statement Sections >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class StatementSections(models.Model):
    FinStatementsFK = models.ForeignKey(
        'FinStatements', null=True, blank=True, on_delete=models.CASCADE)
    SSPersonFK = models.ForeignKey(
        PersonM, null=True, on_delete=models.CASCADE)
    SSName = models.CharField(max_length=240, default='')
    SSDescription = models.CharField(max_length=960, default='')

    def __str__(self):
        return self.SSName

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Section Lines >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class SectionLines(models.Model):
    SLStatementSectionsFK = models.ForeignKey(
        'StatementSections', null=True, blank=True, on_delete=models.CASCADE, related_name='statementsectionlines_set')
    SLPersonFK = models.ForeignKey(
        PersonM, null=True, on_delete=models.CASCADE)
    SLName = models.CharField(max_length=240)
    SLDescription = models.CharField(max_length=240)

    def __str__(self):
        return self.SLName

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Line Accounts >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class LineAccounts(models.Model):
    LAStatementLineFK = models.ForeignKey(
        'SectionLines', null=True, blank=True, on_delete=models.CASCADE, related_name='statementlineaccounts_set')
    LAPersonFK = models.ForeignKey(
        PersonM, null=True, on_delete=models.CASCADE)
    LAAccount = models.IntegerField()
    LAAccountType = models.CharField(max_length=12)
    LAADescription = models.CharField(max_length=240)

    def __str__(self):
        return self.LAAccount

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CashInAcctM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class CashInAcctM(models.Model):
    Status = models.CharField(max_length=10, null=True)
    AccountNumber = models.CharField(max_length=20, null=True)
    Description = models.CharField(max_length=255, null=True)
    Type = models.CharField(max_length=12, null=True)
    Sequence = models.IntegerField(null=True)
    RollupType = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.AccountNumber

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TransBatch >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class TransBatch(models.Model):
    TransBatchName = models.CharField(max_length=120, null=True, unique=True)
    TransBatchDate = models.DateField(null=True)
    Created = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.TransBatchName

    class Meta:
        verbose_name_plural = 'Transaction Batch'

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TransHeader >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class TransHeader(models.Model):
    TransBatchID = models.ForeignKey(
        'TransBatch', null=True, on_delete=models.CASCADE)
    TransDescription = models.CharField(max_length=120, null=True)
    TransDate = models.DateField(null=True)
    TransNote = models.CharField(max_length=240, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Transaction Header'

    def __str__(self):
        return self.TransDescription

# *******************************************************************************
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TransDetail >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# *******************************************************************************


class TransDetail(models.Model):
    TransHeaderID = models.ForeignKey(
        'TransHeader', null=True, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    DrAccount = models.CharField(max_length=10, null=True)
    CrAccount = models.CharField(max_length=10, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Transaction Detail'

    def __str__(self):
        return self.Amount
