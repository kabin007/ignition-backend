# Generated by Django 5.1.4 on 2025-01-13 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_basicinfo_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicinfo',
            old_name='maritalStatus',
            new_name='marital_status',
        ),
    ]
