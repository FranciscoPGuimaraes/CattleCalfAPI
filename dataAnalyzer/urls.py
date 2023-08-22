from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('create', createWeight),
    path('weight', cattleWeight),
]