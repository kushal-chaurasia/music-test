from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from .serializers import SongSerializer, AudiobookSerializer, PodcastSerializer
from .models import Audiobook, Song, Podcast


# Create your views here.
class AudioFileView(APIView):
    model_class = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        output_status = False
        output_detail = "Fail"
        res_status = HTTP_400_BAD_REQUEST
        output_data = {}
        id = request.GET.get("id")
        obj = self.model_class.objects.filter(pk = id).first()
        if obj:
            serializer = self.serializer_class(obj)
            output_data = serializer.data
            output_status = True
            output_detail = "Success"
            res_status = HTTP_200_OK

        else:
            output_detail = "Invalid Id"
        context = {
            "status" : output_status,
            "detail" : output_detail,
            "data" : output_data
        }
        return Response (context, status=res_status, content_type="application/json")

    def post(self, request, *args, **kwargs):
        output_status = False
        output_detail = "Fail"
        res_status = HTTP_400_BAD_REQUEST
        output_data = {}
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            output_status = True
            output_detail = "Success"
            res_status = HTTP_200_OK
        else:
            output_data = serializer.errors
        context = {
            "status" : output_status,
            "detail" : output_detail,
            "data" : output_data
        }
        return Response (context, status=res_status, content_type="application/json")

    def put(self, request):
        output_status = False
        output_detail = "Fail"
        res_status = HTTP_400_BAD_REQUEST
        output_data = {}
        id = request.data.get("id")
        if id:
            obj = self.model_class.objects.filter(pk = id).first()
            if obj:
                serializer = self.serializer_class(obj,data = request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    output_status = True
                    output_detail = "Success"
                    res_status = HTTP_200_OK
                else:
                    output_data = serializer.errors
            else:
                output_detail = "invalid id"
        else:
            output_detail = "Id is required parameter"
        context = {
            "status" : output_status,
            "detail" : output_detail,
            "data" : output_data
        }
        return Response (context, status=res_status, content_type="application/json")
        

    def delete(self, request):
        output_status = False
        output_detail = "Fail"
        res_status = HTTP_400_BAD_REQUEST
        output_data = {}
        id = request.data.get("id")
        if id:
            obj = self.model_class.objects.filter(pk = id).first()
            if obj:
                obj.delete()
                output_status = True
                output_detail = "Success"
                res_status = HTTP_200_OK
            else:
                output_detail = "Invalid ID"
        else:
            output_detail = "Id is required parameter"
        context = {
            "status" : output_status,
            "detail" : output_detail,
            "data" : output_data
        }
        return Response (context, status=res_status, content_type="application/json")


class SongView(AudioFileView):
    model_class = Song
    serializer_class = SongSerializer

class PodcastView(AudioFileView):
    model_class = Podcast
    serializer_class= PodcastSerializer

class AudiobookView(AudioFileView):
    model_class = Audiobook
    serializer_class = AudiobookSerializer