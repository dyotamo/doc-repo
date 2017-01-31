from django.contrib import admin

from .models import Place

# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

	list_display	= ['name', 'category', 'city', 'address', 'is_working',]
	list_per_page	= 10

	fields			= [('name', 'city',), ('address',), ('tel1', 'tel2',),
							('fax', 'email',), ('lat',), ('lng',), ('category',
									'image',), ('e1', 's1'), ('e2', 's2'),]
