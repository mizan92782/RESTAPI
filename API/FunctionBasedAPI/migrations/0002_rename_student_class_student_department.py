# Generated by Django 5.2.4 on 2025-07-24 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FunctionBasedAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_class',
            new_name='department',
        ),
    ]
