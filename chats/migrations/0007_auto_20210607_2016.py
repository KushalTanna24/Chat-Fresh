# Generated by Django 3.2.4 on 2021-06-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_alter_profile_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userprofile',
        ),
    ]
