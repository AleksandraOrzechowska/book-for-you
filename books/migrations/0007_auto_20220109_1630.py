# Generated by Django 3.1.7 on 2022-01-09 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='author_second_name',
            new_name='second_name',
        ),
    ]
