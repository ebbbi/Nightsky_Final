# Generated by Django 3.0.2 on 2020-01-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_deletetoreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletetoreport',
            name='writer',
        ),
        migrations.AddField(
            model_name='deletetoreport',
            name='report',
            field=models.TextField(default=''),
        ),
    ]