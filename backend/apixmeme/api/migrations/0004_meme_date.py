# Generated by Django 3.1.6 on 2021-02-08 21:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210208_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
