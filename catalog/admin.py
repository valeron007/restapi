import requests
from django.contrib import admin

# Register your models here.

from .models import (Category, Product, CurrencyRate)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):

    actions = ['update_currency_rate']

    def update_currency_rate(self, request, queryset):
        for rate in queryset:
            pair = "{}RUB".format(rate.currency.upper())
            response = requests.get(
                "https://www.freeforexapi.com/api/live?pairs={}".format(pair)
            )
            data = response.json()







