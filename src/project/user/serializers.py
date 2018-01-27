from rest_framework import serializers
from project.user.models import Citizen, Preference

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('user', 'birthdate', 'city', 'onboard_answer_1', 'onboard_answer_2')

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ('name')