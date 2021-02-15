from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# this is basically the schema(rows & column) of database
# meme model with name, caption, url and date
class Meme(models.Model):
    name = models.CharField(max_length=100, default='Anamika' )     #name of person who is uploading the meme
    caption = models.CharField(max_length=100, default='Meme Caption' )  #caption of meme
    url = models.CharField(max_length=300, default='https://resize.indiatvnews.com/en/resize/newbucket/1200_-/2020/02/valentine-day-memes-1581658432.jpg')  #url of meme
    date = models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return self.name      