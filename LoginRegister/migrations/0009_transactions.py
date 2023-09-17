# Generated by Django 4.2.4 on 2023-08-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0008_calendars_dates_defaultparams_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]