# Generated by Django 3.2.4 on 2021-06-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_remove_profile_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
