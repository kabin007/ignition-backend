# Generated by Django 5.1.4 on 2025-01-12 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_courselevel_faculty_remove_course_level_and_more'),
        ('university', '0002_remove_course_category_remove_course_university_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate'), ('Diploma', 'Diploma'), ('Certificate', 'Certificate')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='intakes',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculty', to='course.faculty'),
        ),
        migrations.AlterField(
            model_name='course',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university', to='university.university'),
        ),
    ]
