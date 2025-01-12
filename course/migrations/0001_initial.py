# Generated by Django 5.1.4 on 2025-01-09 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0002_remove_course_category_remove_course_university_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prerequisites', models.TextField()),
                ('credits', models.IntegerField()),
                ('start_date', models.DateField()),
                ('application_deadline', models.DateField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university', to='university.university')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='course.courselevel')),
            ],
        ),
    ]
