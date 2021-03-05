from django.contrib import admin
from .models import Expense, Income, Token

# Register your models here.
admin.site.register(model_or_iterable=Expense)
admin.site.register(model_or_iterable=Income)
admin.site.register(model_or_iterable=Token)
