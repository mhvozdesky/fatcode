# Generated by Django 4.0.6 on 2022-07-14 11:27

from django.db import migrations, models
import src.profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=src.profiles.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='fatuser',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
