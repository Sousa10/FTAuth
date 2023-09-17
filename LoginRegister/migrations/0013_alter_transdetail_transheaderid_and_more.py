# Generated by Django 4.2.4 on 2023-09-02 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0012_alter_transbatch_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transdetail',
            name='TransHeaderID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LoginRegister.transheader'),
        ),
        migrations.AlterField(
            model_name='transheader',
            name='TransBatchID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LoginRegister.transbatch'),
        ),
    ]