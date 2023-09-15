"""
Views from users
@author Francisco P. Guimarães
@since 05/09/23
"""
import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.serializers import *
from users.models import *


@api_view(['POST'])
def register(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        if 'user' in body:
            user_data = body['user']
            userSerializer = UserSerializer(data=user_data)
        else:
            return Response({"error": "user field not found"}, status.HTTP_400_BAD_REQUEST)

        if userSerializer.is_valid():
            email = body["user"]["email"]
            emailExists = User.objects.filter(email=email)
            if not emailExists:
                userSerializer.validated_data["password"] = make_password(userSerializer.validated_data["password"])
                userSerializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": userSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        login = LoginSerializer(data=body['login'])

        if login.is_valid():
            email = login.data.get("email")
            password = login.data.get("password")
            user = User.objects.get(email=email)
            userSerializer = LoginSerializer(user)
            if user:
                if check_password(password, userSerializer.data["password"]):
                    return Response(status=status.HTTP_202_ACCEPTED)
                return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"error": "Email not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(login.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
