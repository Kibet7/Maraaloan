# Generated by Django 5.0.7 on 2024-12-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_user_alter_loanapplication_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_expiry',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_request_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
