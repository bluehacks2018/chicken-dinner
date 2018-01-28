from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from project.user.models import Citizen, Preference
from project.user.serializers import CitizenSerializer, PreferenceSerializer, UserSerializer

from rest_framework.views import APIView

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class CitizenList(APIView):
    def get(self, request, format=None):
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens, many=True)
        response = Response(serializer.data)
        response['test'] = "hi"
        return response

    def post(self, request, format=None):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PreferenceList(APIView):
    def get(self, request, format=None):
        preferences = Preference.objects.all()
        serializer = PreferenceSerializer(citizens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CitizenDetail(APIView):
    def get_object(self, pk):
        try:
            return Citizen.objects.get(user=pk)
        except Citizen.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        citizen = self.get_object(pk)
        citizen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PreferenceDetail(APIView):
    def get_object(self, pk):
        try:
            return Preference.objects.get(pk=pk)
        except Preference.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        preference = self.get_object(pk)
        serializer = PreferenceSerializer(preference)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        preference = self.get_object(pk)
        serializer = PreferenceSerializer(preference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        preference = self.get_object(pk)
        preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CitizenPref(APIView):
    def get_object(self, name):
        try:
            return Citizen.objects.get(user=name)
        except Citizen.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        Citizen = self.get_object(user=name)
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)


@api_view(['POST'])
def create(request):

    if request.method == 'POST':
        serializer = CitizenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)
