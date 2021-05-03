from django.contrib import admin
from .models import Podcast, Audiobook, Song

# Register your models here.

admin.site.register(Podcast)
admin.site.register(Audiobook)
admin.site.register(Song)
