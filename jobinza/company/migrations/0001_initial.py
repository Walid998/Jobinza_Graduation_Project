# Generated by Django 2.2.10 on 2020-03-09 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jobRole',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='relatedIndustry',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('name', models.CharField(max_length=70, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(blank=True, max_length=50)),
                ('job_description', models.CharField(blank=True, max_length=500)),
                ('joblocation', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('Area', models.CharField(blank=True, max_length=50)),
                ('careerlevel', models.CharField(blank=True, max_length=50)),
                ('year_of_experience', models.CharField(blank=True, max_length=50)),
                ('salary_range1', models.CharField(blank=True, max_length=50)),
                ('salary_range2', models.CharField(blank=True, max_length=50)),
                ('num_vacancies', models.TextField(blank=True, max_length=50)),
                ('jobtype', models.CharField(blank=True, max_length=50)),
                ('deadline', models.DateField()),
                ('status', models.CharField(default='Publishing', max_length=10)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('related_industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.relatedIndustry')),
                ('rolejob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.jobRole')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.skills')),
            ],
        ),
    ]
