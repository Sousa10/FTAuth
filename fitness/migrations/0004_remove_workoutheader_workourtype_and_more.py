# Generated by Django 4.2.4 on 2023-10-12 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_workoutheader_workourtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutheader',
            name='WorkourType',
        ),
        migrations.AddField(
            model_name='workoutheader',
            name='WorkoutType',
            field=models.CharField(max_length=80, null=True),
        ),
    ]