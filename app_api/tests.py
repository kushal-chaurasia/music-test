from django.test import TestCase
from rest_framework.test import APITestCase
from . models import Song, Podcast, Audiobook
from rest_framework.test import APIRequestFactory
# Create your tests here.


class SongViewTestCase(APITestCase):

    url = '/api/music/song/'

    def setUp(self):
        Song.objects.create(name="Test Data",duration = 250 )

    def test_post_songview(self):
        data = {
        "name" : "test Data",
        "duration": 120,
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)



    def test_get_songview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_delete_songview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_put_songview(self):
        data = {
            'id' : 1,
            'name' : "Test Change",
            'duration' : 200,
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

        
class PodcastViewTest(APITestCase):
    url = '/api/music/podcast/'

    def setUp(self):
        Podcast.objects.create(name="Test Data",duration = 250, host = "test Host", participant = 'a,b,c,d,e' )

    def test_post_podcastview(self):
        data = {
        "name" : "test Data",
        "duration": 120,
        "host" : "test host",
        "participant" : 'a,b,c,d,e',
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)



    def test_get_podcastview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_delete_podcastview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_put_podcastview(self):
        data = {
            'id' : 1,
            'name' : "Test Change",
            'duration' : 200,
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)




class AudiobookViewTest(APITestCase):
    url = '/api/music/audiobook/'

    def setUp(self):
        Audiobook.objects.create(name="Test Data",duration = 250,author = "test", narrator="Test")

    def test_post_audiobookview(self):
        data = {
        "name" : "test Data",
        "duration": 120,
        "author": "test", 
        "narrator":"Test",
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)



    def test_get_audiobookview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_delete_audiobookview(self):
        data = {
            'id' : 1
        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)

    def test_put_audiobookview(self):
        data = {
            'id' : 1,
            'duration' :240,
            "author": "test", 
            "narrator":"Test",

        }
        response = self.client.get(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,dict)
        self.assertEqual(result["status"],True)



factory = APIRequestFactory()
song_data = {
    "name" : "test Data",
    "duration": 120,
}
request = factory.post('/api/music/song/', song_data,  format='json')
podcast_data = {
        "name" : "test Data",
        "duration": 120,
        "host" : "test host",
        "participant" : 'a,b,c,d,e',
        }
request = factory.get('/api/music/podcast/', podcast_data,  format='json' )

audiobook_data = {
        "name" : "test Data",
        "duration": 120,
        "author": "test", 
        "narrator":"Test",
        }
request = factory.get('/api/music/audiobook/', audiobook_data,  format='json' )