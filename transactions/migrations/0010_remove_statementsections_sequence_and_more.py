# Generated by Django 4.2.4 on 2023-12-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_alter_cashinacctm_options_cashinacctm_rolluptype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statementsections',
            name='Sequence',
        ),
        migrations.AlterField(
            model_name='statementsections',
            name='LineName',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='statementsections',
            name='StatementType',
            field=models.CharField(max_length=80, null=True),
        ),
    ]