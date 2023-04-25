from django.urls import path

from . import views

urlpatterns = [
    path("", views.posts),
    path("<pk>", views.post),
    path("<postid>/comments", views.postcomments),
    path("<postid>/likes", views.postlikes),
    path("<postid>/comments/<commentid>", views.postcomment),
    path("<postid>/likes/<likeid>", views.postlike),
]
