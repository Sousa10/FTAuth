# Generated by Django 4.2.1 on 2023-08-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0004_sponrates'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarIncrements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sequence', models.IntegerField(max_length=10, null=True)),
                ('FamilyID', models.IntegerField(max_length=10, null=True)),
                ('PersonID', models.IntegerField(max_length=10, null=True)),
                ('CalendarID', models.CharField(max_length=120, null=True)),
                ('IncrementDate', models.DateField()),
                ('IncrementTime', models.TimeField()),
            ],
        ),
    ]
