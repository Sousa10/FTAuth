# Generated by Django 4.2.4 on 2023-11-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_statementsections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statementsections',
            name='LineName',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
