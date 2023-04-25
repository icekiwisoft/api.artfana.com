from django.urls import path

from . import views

urlpatterns = [
    path("register", views.posts),
    path("login", views.post),
    path("<userid>/posts", views.postcomments),
    path("<userid>/likedposts", views.postlikes),
    path("<userid>/commentedposts", views.postlikes),
    path("<userid>")


]
