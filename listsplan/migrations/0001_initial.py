# Generated by Django 4.2.6 on 2023-12-01 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListHeaderT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LHName', models.CharField(max_length=240)),
                ('LHDescription', models.CharField(max_length=240)),
                ('PersonFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListDetailsT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LNNumber', models.IntegerField()),
                ('LHName', models.CharField(max_length=240)),
                ('ListDetailFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='predecessor', to='listsplan.listdetailst')),
                ('ListHeaderFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listsplan.listheadert')),
            ],
        ),
    ]
