# Generated by Django 4.2.4 on 2023-09-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='admin',
            new_name='room_admin',
        ),
    ]
