# Generated by Django 5.1.1 on 2024-09-25 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
