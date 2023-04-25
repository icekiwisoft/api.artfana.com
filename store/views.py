from django.shortcuts import render

# Create your views here.

@api_view(['GET','POST'])
def store(request):
    if request.method=="GET":
        posts = objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        pass

def storeitem(request,pk):
    if request.method=="GET":
        posts = objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        pass