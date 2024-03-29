# Generated by Django 5.0 on 2024-02-06 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0019_statementsections_finstatementfk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statementlinesline',
            name='SLStatementLineFK',
        ),
        migrations.RemoveField(
            model_name='statementlinesline',
            name='SLStatementSectionFK',
        ),
        migrations.RenameField(
            model_name='statementsections',
            old_name='FinStatementFK',
            new_name='FinStatementsFK',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSBalanceSheetStatementSequence',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSBalanceSheetStatementYN',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSBudgetStatementSequence',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSBudgetStatementYN',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSCashFlowStatementSequence',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSCashFlowStatementYN',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSExpenseStatementSequence',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSExpenseStatementYN',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSIncomeStatementSequence',
        ),
        migrations.RemoveField(
            model_name='statementsections',
            name='SSIncomeStatementYN',
        ),
        migrations.AddField(
            model_name='finstatements',
            name='FSPersonFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.personm'),
        ),
        migrations.CreateModel(
            name='SectionLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SLName', models.CharField(max_length=240)),
                ('SLDescription', models.CharField(max_length=240)),
                ('SLPersonFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.personm')),
                ('SLStatementSectionsFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.statementsections')),
            ],
        ),
        migrations.CreateModel(
            name='LineAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LAAccount', models.IntegerField()),
                ('LAAccountType', models.CharField(max_length=12)),
                ('LAADescription', models.CharField(max_length=240)),
                ('LAPersonFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.personm')),
                ('LAStatementLineFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statementlineaccounts_set', to='transactions.sectionlines')),
            ],
        ),
        migrations.DeleteModel(
            name='StatementLineAccounts',
        ),
        migrations.DeleteModel(
            name='StatementLinesLine',
        ),
    ]
