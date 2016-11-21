from django.contrib import admin

from .models import Pharmacy

# Register your models here.

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):

	list_display = ['name', 'city', 'address', 'working',]