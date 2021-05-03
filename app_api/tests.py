from django.test import TestCase
from rest_framework.test import APITestCase
from . models import Song
from django.utils import timezone

# Create your tests here.


class SongViewTestCase(APITestCase):

    url = '/api/music/song/'

    def setUp(self):
        Song.objects.create(name="Test Data",duration = 250 )


    def test_get_songview(self):
        response = self.client.get(self.url)

