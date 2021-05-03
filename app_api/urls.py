from django.urls import path
from .views import SongView, AudiobookView, PodcastView

urlpatterns = [
    path('podcast/', PodcastView.as_view()),
    path('song/', SongView.as_view()),
    path('audiobook/', AudiobookView.as_view()),
]