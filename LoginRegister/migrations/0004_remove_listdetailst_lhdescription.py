# Generated by Django 4.2.2 on 2023-08-09 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0003_acctrollupsd_transactionst_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listdetailst',
            name='LHDescription',
        ),
    ]