# Generated by Django 4.2.4 on 2023-08-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0010_transdetail_transheader_delete_transactionst'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransBatchName', models.CharField(max_length=120, null=True)),
                ('TransBatchDate', models.DateField()),
                ('Created', models.DateField()),
                ('LastUpdated', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='transheader',
            name='TransBatchID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transdetail',
            name='TransHeaderID',
            field=models.IntegerField(null=True),
        ),
    ]
