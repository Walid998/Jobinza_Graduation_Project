# Generated by Django 2.2.11 on 2020-07-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0026_match_results_company_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_results',
            name='company_id',
        ),
    ]
