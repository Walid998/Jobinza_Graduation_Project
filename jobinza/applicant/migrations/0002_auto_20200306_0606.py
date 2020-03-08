# Generated by Django 2.2.10 on 2020-03-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]