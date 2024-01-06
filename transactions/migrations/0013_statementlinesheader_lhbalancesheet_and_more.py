# Generated by Django 5.0 on 2024-01-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_statementlinesheader_statementlinesdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBalanceSheet',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBalanceSheetSection',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBalanceSheetSequence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBudgetPerformance',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBudgetPerformanceSection',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHBudgetPerformanceSequence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHCashFlowAnalysis',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHCashFlowAnalysisSection',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHCashFlowAnalysisSequence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHExpenseAnalysis',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHExpenseAnalysisSection',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHExpenseAnalysisSequence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHIncomeStatement',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHIncomeStatementSection',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='statementlinesheader',
            name='LHIncomeStatementSequence',
            field=models.IntegerField(null=True),
        ),
    ]
