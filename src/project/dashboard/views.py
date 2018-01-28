from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from project.dashboard.models import Dataset
from project.user.models import Preference

from project.dashboard.serializers import DatasetSerializer
from project.user.serializers import PreferenceSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class SearchDataset(APIView):
    def get(self, request, tag):
        tags = tag.split()
        tagss = ['a', 'ab', 'c']
        datasets = Dataset.objects.filter(Q(tag__in=tags) | Q(name__in=tags))
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)



# class PopulateDataset(APIView):
#     def get_object(self, pk):
#         try:
#             return Dataset.objects.get(name=pk)
#         except Dataset.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         dataset = self.get_object(name=pk)
#         serializer = Datasetserializer(dataset)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         dataset = Dataset.objects.get(name=pk)
#         dataset.tags = [1, 2]
#         serializer = DatasetSerializer(dataset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def dashboard_feed(request):
    if request.method == 'GET':
        user_id = request.GET['id']
        datasets = Dataset.objects.get_feed(user_id)
        serializers = DatasetSerializer(datasets, many=True)

        return Response(serializers.data)
