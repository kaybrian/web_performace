from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.PostList.as_view(), name="posts"),
    path("post-twice/", views.PostsTwice.as_view(), name="posts_twice"),
    path("post-third/", views.PostThird.as_view(), name="posts_third"),
]

