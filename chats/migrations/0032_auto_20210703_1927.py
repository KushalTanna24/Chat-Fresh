# Generated by Django 2.0 on 2021-07-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0031_auto_20210703_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(default='', max_length=1200),
        ),
    ]
