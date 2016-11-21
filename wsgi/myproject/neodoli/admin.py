from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Pharmacy

# Register your models here.

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):

	list_display = ['name', 'city', 'address', 'working',]

# Remove Auth Group from the admin
admin.site.unregister(Group)