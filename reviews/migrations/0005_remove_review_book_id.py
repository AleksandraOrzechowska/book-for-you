# Generated by Django 3.1.7 on 2022-01-09 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_id',
        ),
    ]
