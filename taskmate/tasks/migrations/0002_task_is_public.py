# Generated by Django 5.1 on 2024-09-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
