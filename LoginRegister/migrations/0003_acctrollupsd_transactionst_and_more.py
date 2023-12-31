# Generated by Django 4.2.2 on 2023-07-26 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LoginRegister', '0002_alter_cashinacctm_accountnumber_listheadert_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcctRollupsD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollUpName', models.CharField(max_length=255, null=True)),
                ('AcctType', models.CharField(max_length=80, null=True)),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCr', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='acctrollupsm',
            name='Statement',
        ),
        migrations.AlterField(
            model_name='listheadert',
            name='PersonFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
