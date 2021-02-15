from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Meme
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MemeSerializer


@api_view(['GET'])
def index(request):  # main page to show the api map
    context = {
        'To post a meme' : '/memes',
        'To get last 100 memes' : '/memes',
        'To get details of a particular meme' : '/memes/id'
    }
    return Response(context)


@api_view(['GET', 'POST'])
def meme(request):

    if request.method == 'GET': 
        memes = Meme.objects.all().order_by('-id')[:100] #extracting latest 100 memes
        serializer = MemeSerializer(memes,many=True) #serializing the memes
        return Response(serializer.data)

    elif request.method == 'POST':  # saving the data(if valid) for post request
        serializer = MemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



@api_view(['GET'])
def particularmeme(request ,id):
    meme = Meme.objects.filter(id=id)
    if not meme.exists():  # check if meme exist
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND) # return "404 not found" response
    serializer = MemeSerializer(meme,many=True)  #serializing the memes
    return Response(serializer.data)
