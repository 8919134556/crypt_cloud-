# Generated by Django 3.2.8 on 2022-06-28 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_User_Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(db_column='user_name', max_length=50, verbose_name='User_Name')),
                ('user_lastname', models.CharField(db_column='user_lastname', max_length=50, verbose_name='User_Lastname')),
                ('gender', models.CharField(db_column='gender', max_length=50, verbose_name='Gender')),
                ('date_of_birth', models.DateField(db_column='date_of_birth', verbose_name='Date_Of_Birth')),
                ('user_phone', models.BigIntegerField(db_column='user_phone', verbose_name='User_Phone')),
                ('user_email', models.EmailField(blank=True, db_column='user_email', max_length=100, null=True, verbose_name='User_Email')),
                ('user_pwd', models.CharField(db_column='user_pwd', max_length=100, verbose_name='User_Password')),
                ('user_image', models.FileField(blank=True, db_column='user_image', upload_to='User/Profile-image/', verbose_name='User_Image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Data_User_Register',
            },
        ),
    ]
