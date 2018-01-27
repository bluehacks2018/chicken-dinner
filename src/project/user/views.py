from django.shortcuts import render

from rest_framework import status
from rest_framework import api_view
from rest_framework import Response

from user.models import Citizen, Preference
from user.serializers import CitizenSerializer, PreferenceSerializer

#Return list of all Citizens
@api_view(['GET, POST'])
def citizen_list(request):
    if request.method == 'GET':
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#Return list of all Preferences
@api_view(['GET', 'POST'])
def preference_list(request):
    if request.method == 'GET':
        preferences = Preference.objects.all()
        serializer = PreferenceSerializer(preferences)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PreferenceSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
#Return single citizen
@api_view(['GET', 'PUT', 'DELETE'])
def citizen_detail(request, pk):
    try:
        citizen = Citizen.objects.get(pk=pk)
    except Citizen.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)

    elif request.method = 'PUT':
        serializer = CitizenSerializer(citizen, data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        citizen.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#Return single preference
@api_view(['GET', 'PUT', 'DELETE'])
def preference_detail(request, pk):
    try:
        preference = Preference.objects.get(pk=pk)
    except Preference.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PreferenceSerializer(preference)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PreferenceSerializer(preference, data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE'
        preference.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)






# Create your views here.
