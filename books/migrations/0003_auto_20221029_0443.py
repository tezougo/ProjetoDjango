# Generated by Django 3.2.16 on 2022-10-29 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_book_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='publishing_company',
            new_name='publish_company',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='release_year',
            new_name='release_date',
        ),
    ]
