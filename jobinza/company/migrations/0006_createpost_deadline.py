# Generated by Django 2.2.10 on 2020-02-27 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_remove_createpost_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpost',
            name='deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]