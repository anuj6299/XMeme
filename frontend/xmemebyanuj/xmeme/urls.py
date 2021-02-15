from django.urls import path
from . import views

app_name = 'xmeme'

urlpatterns = [
    path('home', views.index, name='index'),
    path('', views.postmeme, name='postmeme'),
]