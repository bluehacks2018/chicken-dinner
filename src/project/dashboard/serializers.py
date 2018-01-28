from project.dashboard.models import Dataset, Tag
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class DatasetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
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
            'data',
            'tags'
        )
