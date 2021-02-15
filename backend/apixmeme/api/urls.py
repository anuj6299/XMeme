from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),  #home page to show the url map
    path('memes/', views.meme, name='meme'), #show latest 100 memes and can make post request to save new meme
    path('memes/<int:id>', views.particularmeme, name='particularmeme'), #to show details of particular meme
]