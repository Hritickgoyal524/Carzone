# Generated by Django 2.2.7 on 2021-12-08 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20211208_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='car_titles',
            new_name='car_title',
        ),
    ]
