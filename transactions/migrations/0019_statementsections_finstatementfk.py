# Generated by Django 5.0 on 2024-02-04 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_rename_scurrentdate_finstatements_fscurrentdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementsections',
            name='FinStatementFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.finstatements'),
        ),
    ]
