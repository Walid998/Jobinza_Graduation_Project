# Generated by Django 2.2.11 on 2020-03-29 22:18

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpost',
            name='image',
            field=models.ImageField(blank=True, upload_to=company.models.upload_location),
        ),
    ]