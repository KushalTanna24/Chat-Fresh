# Generated by Django 2.2.24 on 2021-06-13 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0012_auto_20210613_2357'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGroups',
        ),
    ]