# Generated by Django 4.0.4 on 2022-06-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_data', '0002_alter_studentbio_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='uid',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
