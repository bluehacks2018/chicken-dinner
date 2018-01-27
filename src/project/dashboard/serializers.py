from project.dashboard.models import Dataset
from rest_framework import serializers

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'id',
            'name',
            'url', 
            'rating', 
            'popularity', 
            'data'
        )
