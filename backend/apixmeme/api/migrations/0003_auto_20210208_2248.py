# Generated by Django 3.1.6 on 2021-02-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210208_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='caption',
            field=models.CharField(default='Meme Caption', max_length=100),
        ),
        migrations.AlterField(
            model_name='meme',
            name='name',
            field=models.CharField(default='Anamika', max_length=100),
        ),
        migrations.AlterField(
            model_name='meme',
            name='url',
            field=models.CharField(default='https://resize.indiatvnews.com/en/resize/newbucket/1200_-/2020/02/valentine-day-memes-1581658432.jpg', max_length=300),
        ),
    ]
