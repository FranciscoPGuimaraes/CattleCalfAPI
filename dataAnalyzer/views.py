"""Analyser Views
@author: Francisco Pereira Guimaraes"""
import datetime

from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from dataAnalyzer.models import *
from dataAnalyzer.serialyzer import *


@api_view(['GET'])
def home(request):
    """
    This function show all analysis
    :return: all available analysis in the application
    """
    return Response({"Available analysis": ["No analysis yet"]}, status.HTTP_200_OK)


@api_view(['POST'])
def createWeight(request):
    try:
        weight_data = {'weight': 200, 'date': datetime.date.today()}
        weight_serializer = WeightSerializer(data=weight_data)
        if weight_serializer.is_valid():
            weight_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(weight_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({"Exception": str(err)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def cattleWeight(request):
    """
    This function calculate weight statistics
    """
    try:
        weight = Weighing.objects.all()
        weightSerialyzer = WeightSerializer(weight, many=True)
        return Response(weightSerialyzer.data, status.HTTP_200_OK)
    except Exception as err:
        return Response({"Except": "Data lookup error " + str(err)})

