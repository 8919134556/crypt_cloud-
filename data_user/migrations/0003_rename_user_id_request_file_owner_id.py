# Generated by Django 3.2.8 on 2022-06-29 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0002_request_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_file',
            old_name='user_id',
            new_name='owner_id',
        ),
    ]
