from project.dashboard.models import Dataset
from rest_framework import serializers

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'id',
            'name',
            'url',
            'tag',
            'gov_org',
            'chart_type',
            'description', 
            'rating', 
            'popularity',
            'score', 
            'data'
        )
