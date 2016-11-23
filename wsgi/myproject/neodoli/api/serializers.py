from rest_framework import serializers

from neodoli.models import Place

class PlaceSerializer(serializers.ModelSerializer):

	""" Pharmacies serializer """

	working = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()
	category = serializers.SerializerMethodField()

	def get_working(self, obj):
		return obj.working()

	def get_city(self, obj):
		return obj.get_city_display()

	def get_category(self, obj):
		return obj.get_category_display()

	class Meta:
		model = Place
