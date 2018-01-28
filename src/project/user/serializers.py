from rest_framework import serializers
from project.user.models import Citizen, Preference
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ('name')

class CitizenSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer(many=True, read_only = True)
    class Meta:
        model = Citizen
        fields = (
            'user', 
            'birthdate', 
            'city', 
            'onboard_answer_1', 
            'onboard_answer_2', 
            'preferences'
        )