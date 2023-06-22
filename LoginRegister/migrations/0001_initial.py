# Generated by Django 4.2.1 on 2023-06-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcctRollupsM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollUpName', models.CharField(max_length=255, null=True)),
                ('Statement', models.CharField(max_length=255, null=True)),
                ('AcctType', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CashInAcctM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CashOutAcctM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DebtsAcctM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NetworthAcctM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationID', models.IntegerField(null=True)),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('MiddleName', models.CharField(max_length=255, null=True)),
                ('Salutation', models.CharField(max_length=40, null=True)),
                ('NameSuffix', models.CharField(max_length=120, null=True)),
                ('Sex', models.CharField(max_length=40, null=True)),
                ('EdDegree1', models.CharField(max_length=40, null=True)),
                ('EdMajor1', models.CharField(max_length=80, null=True)),
                ('EdDegree2', models.CharField(max_length=40, null=True)),
                ('EdMajor2', models.CharField(max_length=80, null=True)),
                ('DateJoinedTracker', models.DateField(auto_now_add=True)),
                ('EmailPrimary', models.CharField(max_length=255, null=True)),
                ('PostalCodePrimary', models.CharField(max_length=40, null=True)),
                ('PhonePrimary', models.CharField(max_length=40, null=True)),
                ('EmailSecondary', models.CharField(max_length=255, null=True)),
                ('PostalCodeSecondary', models.CharField(max_length=40, null=True)),
                ('PhoneSecondary', models.CharField(max_length=40, null=True)),
                ('FTUserName', models.CharField(max_length=80, null=True)),
                ('Password', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='WhatWeOwnAcctM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountNumber', models.CharField(max_length=40, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('DrCrBal', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
