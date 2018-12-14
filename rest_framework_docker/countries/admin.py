from django.contrib import admin
from .models import Country


@admin.register(Country)
class countryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['name', 'code']