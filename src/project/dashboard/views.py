from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.dashboard.models import Dataset
from project.dashboard.serializers import DatasetSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


@api_view(['GET'])
def dashboard_feed(request):
    if request.method == 'GET':
        user_id = request.GET['id']
        datasets = Dataset.objects.get_feed(user_id)
        serializers = DatasetSerializer(datasets, many=True)

        return Response(serializers.data)
