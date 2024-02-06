# Generated by Django 5.0 on 2024-01-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0021_linkclickcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CashInAcctM',
        ),
        migrations.DeleteModel(
            name='CashOutAcctM',
        ),
        migrations.DeleteModel(
            name='DebtsAcctM',
        ),
        migrations.DeleteModel(
            name='NetworthAcctM',
        ),
        migrations.RemoveField(
            model_name='transheader',
            name='TransBatchID',
        ),
        migrations.RemoveField(
            model_name='transdetail',
            name='TransHeaderID',
        ),
        migrations.DeleteModel(
            name='WhatWeOwnAcctM',
        ),
        migrations.DeleteModel(
            name='TransBatch',
        ),
        migrations.DeleteModel(
            name='TransDetail',
        ),
        migrations.DeleteModel(
            name='TransHeader',
        ),
    ]