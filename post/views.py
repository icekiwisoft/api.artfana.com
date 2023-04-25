from django.shortcuts import render
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view

# Create your views here.



@api_view(['GET','POST'])
def posts(request):
    if request.method=="GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        pass


@api_view(['GET','DELETE','PATCH'])
def post(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method=="DELETE":
        post.delete()


@api_view(['GET','POST'])
def postcomments(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method=="DELETE":
        post.delete()



@api_view(['GET','POST'])
def postlikes(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method=="DELETE":
        post.delete()



@api_view(['GET','DELETE','PATCH'])
def postcomment(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method=="DELETE":
        post.delete()





@api_view(['GET','DELETE','PATCH'])
def postlike(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method=="DELETE":
        post.delete()




    


