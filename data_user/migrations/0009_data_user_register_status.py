# Generated by Django 3.2.8 on 2022-07-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0008_download_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_user_register',
            name='status',
            field=models.CharField(db_column='status', default='Pending', max_length=50, null=True, verbose_name='Status'),
        ),
    ]
