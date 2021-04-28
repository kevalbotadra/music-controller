from django.urls import path, include
from .views import *

urlpatterns = [
    path("get-auth-url", AuthUrl.as_view()),
    path("redirect", spotify_callback),
    path("is-authenticated", isAuthenticated.as_view()),
    path("current-song", CurrentSong.as_view()),
]