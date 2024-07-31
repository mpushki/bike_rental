from django.contrib import admin
from bikes.models import Bike


@admin.register(Bike)
class BicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'price', 'rent_is')
    search_fields = ('model',)
