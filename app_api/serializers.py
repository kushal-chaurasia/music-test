from rest_framework import serializers
from .models import Podcast, Audiobook, Song



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields ="__all__"

    def validate_participant(self, value):
        participant_data = value
        participant_list = participant_data.split(',')
        participant_name = []
        if len(participant_list) < 11:
            for data in participant_list:
                if len(data) <101:
                    participant_name.append(data)
                else:
                    raise serializers.ValidationError({"participant": "length cannot exceed the length of 100 character"})
        else:
            raise serializers.ValidationError({"participant": "maximum participant limit is 10"})

        return value

    
    


    
                    




        
