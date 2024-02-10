# Generated by Django 4.2.7 on 2024-02-10 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_logevent_changes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logevent',
            name='user',
        ),
        migrations.AddField(
            model_name='logevent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.student'),
        ),
    ]