# Generated by Django 4.1.1 on 2022-11-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_userposts_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='userbio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('mobile', models.IntegerField(max_length=20)),
                ('profile', models.ImageField(upload_to='profile')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
