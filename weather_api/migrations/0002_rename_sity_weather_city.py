# Generated by Django 4.2.7 on 2024-06-04 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='sity',
            new_name='city',
        ),
    ]