from django.urls import path
from . import views

urlpatterns = [

    path(route='submit/expense/',
         view=views.submit_expense,
         name='submit_expense'),

    path(route='submit/income/',
         view=views.submit_income,
         name='submit_income')

]
