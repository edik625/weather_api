# Generated by Django 4.2.7 on 2024-06-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0002_rename_sity_weather_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
