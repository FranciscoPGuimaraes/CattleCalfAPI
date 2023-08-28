"""
Serializers from Cliente's app
"""
from dataAnalyzer.models import *
from rest_framework import serializers


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weighing
        fields = ['weight', 'date']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['amount', 'date']
