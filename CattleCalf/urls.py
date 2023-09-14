from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dataAnalyzer/', include('dataAnalyzer.urls')),
    path('users/', include('users.urls'))
]
