# Generated by Django 4.1.1 on 2022-09-20 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ipandrequests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipandrequests',
            old_name='created_at',
            new_name='last_request_time',
        ),
    ]