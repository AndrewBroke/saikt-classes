# Generated by Django 4.2.7 on 2024-02-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_remove_logevent_user_logevent_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='target_xp',
            field=models.IntegerField(default=0),
        ),
    ]
