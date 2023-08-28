from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('createWeight', createWeight),
    path('weight', cattleWeight),
    path('createExpense', createExpense),
    path('expense', cattleExpenseWeight),
    path('createType', createExpenseType),
    path('expenseByType', cattleExpenseByType),
]