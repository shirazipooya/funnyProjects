from typing import Text
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import User, Token, Expense, Income
from datetime import datetime

# Create your views here.


def token(request):
    '''User Token'''
    pass


@csrf_exempt
def submit_expense(request):
    """User Submit An Expense"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(
        text=request.POST['text'],
        date=date,
        amount=request.POST['amount'],
        user=this_user
    )

    return JsonResponse(
        {'Status': 'OK'}
    )


@csrf_exempt
def submit_income(request):
    """User Submit An Income"""

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(
        text=request.POST['text'],
        date=date,
        amount=request.POST['amount'],
        user=this_user
    )

    return JsonResponse(
        {'Status': 'OK'}
    )
