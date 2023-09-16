"""Analyser Views
@author: Francisco Pereira Guimaraes
@since 05/09/23"""

import datetime
import numpy as np

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
    return Response({"Available analysis": {"Weight": "http://127.0.0.1:8000/dataAnalyzer/weight",
                                            "Expense": "http://127.0.0.1:8000/dataAnalyzer/expense",
                                            "ExpenseByType": "http://127.0.0.1:8000/dataAnalyzer/expenseByType"}},
                    status.HTTP_200_OK)


@api_view(['POST'])
def createWeight(request):
    try:
        weight_data = {'weight': 300, 'date': datetime.date.today()}
        weight_serializer = WeightSerializer(data=weight_data)
        if weight_serializer.is_valid():
            weight_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(weight_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({"Exception": str(err)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createExpense(request):
    try:
        expense_data = {'amount': 400.00, 'date': datetime.date.today(), 'type_idType': 2}
        expense_serializer = ExpenseSerializer(data=expense_data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(expense_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({"Exception": str(err)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createExpenseType(request):
    try:
        type_data = {"name": "Alimentação"}
        type_serializer = TypeSerializer(data=type_data)
        if type_serializer.is_valid():
            type_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({"Exception": str(err)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cattleWeight(request):
    """
    This function calculate weight statistics
    """
    try:
        data = []

        weight = Weighing.objects.all()
        weightSerialyzer = WeightSerializer(weight, many=True)

        for w in weightSerialyzer.data:
            data.append(w['weight'])

        average = np.average(data)
        variance = np.var(data)
        sdeviations = np.std(data)

        return Response({"Average": average, "Variance": variance, "Standard Deviation": sdeviations, "Data": data},
                        status.HTTP_200_OK)
    except Exception as err:
        return Response({"Except": "Data lookup error " + str(err)})


@api_view(['GET'])
def cattleExpenseWeight(request):
    """
    This function calculate expense/weight
    """
    try:
        totalWeight = 0
        totalExpense = 0

        weight = Weighing.objects.all()
        weightSerialyzer = WeightSerializer(weight, many=True)
        expense = Expense.objects.all()
        expenseSerialyzer = ExpenseSerializer(expense, many=True)

        for w in weightSerialyzer.data:
            totalWeight += w['weight']

        for e in expenseSerialyzer.data:
            totalExpense += e['amount']

        print(f'{totalExpense} {totalWeight}')
        cost = totalExpense / totalWeight

        return Response({"Cost (R$/Kg)": cost, "Expense(R$)": totalExpense, "Weight(Kg)": totalWeight},
                        status.HTTP_200_OK)
    except Exception as err:
        return Response({"Except": "Data lookup error " + str(err)})


@api_view(['GET'])
def cattleExpenseByType(request):
    """This function calculate expense by each type"""
    try:
        type = Type.objects.all()
        typeSerialyzer = TypeSerializer(type, many=True)
        expenseByType = []

        for t in typeSerialyzer.data:
            expense = Expense.objects.filter(type_idType=t['idType'])
            expenseSerialyzer = ExpenseSerializer(expense, many=True)
            total = 0
            for e in expenseSerialyzer.data:
                total += e['amount']
            expenseByType.append({f'{t["name"]}(R$)': total})
        return Response(expenseByType, status.HTTP_200_OK)

    except Exception as err:
        return Response({"Except": "Data lookup error " + str(err)})

@api_view(['POST'])
def syncWeights(request):
    """Synchronizing Database"""

    data = request.data

    for item_data in data:
        date = item_data.get('date')
        weight = item_data.get('weight')

        print(date)

        existing_weight, created = Weighing.objects.update_or_create(
            weight=weight,
            date=date,
            defaults=item_data
        )

    return Response("Weights synchronization completed", status=status.HTTP_201_CREATED)

@api_view(['POST'])
def syncExpense(request):
    """Synchronizing Database"""

    data = request.data

    for item_data in data:
        date = item_data.get('date')
        amount = item_data.get('amount')
        type_idType_id = item_data.get('type_idType')

        try:
            type_instance = Type.objects.get(idType=type_idType_id)
        except Type.DoesNotExist:
            return Response(f"Type com ID {type_idType_id} não existe.", status=status.HTTP_400_BAD_REQUEST)

        existing_expense, created = Expense.objects.update_or_create(
            date=date,
            type_idType=type_instance,
            defaults={'amount': amount}
        )

    return Response("Expense synchronization completed", status=status.HTTP_201_CREATED)

@api_view(['POST'])
def syncTypes(request):
    """Synchronizing Database"""

    data = request.data

    for item_data in data:
        name = item_data.get('name')

        existing_expense, created = Type.objects.update_or_create(
            name=name,
            defaults=item_data
        )

    return Response("Type synchronization completed", status=status.HTTP_201_CREATED)