# Generated by Django 4.0.4 on 2022-06-05 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_data', '0003_studentdata_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='grade',
            field=models.CharField(default='NULL', max_length=10),
        ),
    ]
