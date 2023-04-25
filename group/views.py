from django.shortcuts import render

from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Group
from .serializers import GroupSerializer
from rest_framework.decorators import api_view

# Create your views here.



@api_view(['GET','POST'])
def groups(request):
    if request.method=="GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        pass

@api_view(['GET','DELETE','PATCH'])
def group(request,pk):
    group = Group.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(group)
        return Response(serializer.data)
    if request.method=="DELETE":
        group.delete()

