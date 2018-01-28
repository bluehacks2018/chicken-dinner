from rest_framework import serializers
from project.user.models import Citizen, Preference
from django.contrib.auth.models import User

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ('id', 'name')

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

class UserSerializer(serializers.ModelSerializer):
    # preferences = PreferenceSerializer(many=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class CitizenSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Citizen
        fields = ('user', 'city', 'onboard_answer_1', 'onboard_answer_2', 'preferences')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        citizen, created = Citizen.objects.update_or_create(
            user=user, 
            city=validated_data.pop('city'),
            onboard_answer_1=validated_data.pop('onboard_answer_1'),
            onboard_answer_2=validated_data.pop('onboard_answer_2'),
<<<<<<< HEAD
        )

        for preference in validated_data.pop('preferences'):
            citizen.preferences.add(preference)

        return citizen
=======
        ) 
        
>>>>>>> 19ce0323596ba12df11053e0c6c541d736482beb
