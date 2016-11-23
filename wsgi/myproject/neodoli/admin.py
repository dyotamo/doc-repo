from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Place

# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

	list_display = ['name', 'category', 'city', 'address', 'working',]

# Remove Auth Group from the admin
admin.site.unregister(Group)