# Generated by Django 2.0 on 2021-07-03 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0026_auto_20210703_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(default='', upload_to='file/'),
        ),
        migrations.AlterField(
            model_name='forgotpwd',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 15, 19, 40, 266198)),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 15, 19, 40, 266198)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 15, 19, 40, 265246)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 15, 19, 40, 265246)),
        ),
    ]
