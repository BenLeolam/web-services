# Generated by Django 4.2.7 on 2023-11-22 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='avatar_image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]