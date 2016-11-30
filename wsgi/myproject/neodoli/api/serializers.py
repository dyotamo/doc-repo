from rest_framework import serializers

from neodoli.models import Place

class PlaceSerializer(serializers.ModelSerializer):

	""" Pharmacies serializer """

	city = serializers.SerializerMethodField()
	category = serializers.SerializerMethodField()	

	def get_city(self, obj):
		return obj.get_city_display()

	def get_category(self, obj):
		return obj.get_category_display()

	class Meta:
		model = Place
