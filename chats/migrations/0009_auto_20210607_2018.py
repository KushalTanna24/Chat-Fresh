# Generated by Django 3.2.4 on 2021-06-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_profile_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='userprofile',
            field=models.CharField(default='', max_length=100),
        ),
    ]
