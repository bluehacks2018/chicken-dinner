from rest_framework import serializers
from user.models import Citizen, Preference

class CitizenSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Citizen
        #fields = ('user', 'birthdate', 'city', 'on_board_answer_1', 'on_board_answer_2')

class PreferenceSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Preference
        #fields = ('name')