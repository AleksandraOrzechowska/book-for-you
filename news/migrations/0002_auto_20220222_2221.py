# Generated by Django 3.1.7 on 2022-02-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_name',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='', upload_to='news/'),
        ),
    ]