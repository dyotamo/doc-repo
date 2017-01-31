from rest_framework import serializers

from neodoli.models import Place

class PlaceSerializer(serializers.ModelSerializer):

	""" Pharmacies serializer """

	city = serializers.SerializerMethodField()
	is_working = serializers.SerializerMethodField()

	def get_city(self, obj):
		return obj.get_city_display()

	def get_is_working(self, obj):
		return obj.is_working()

	class Meta:
		model = Place
		exclude = ['e1', 'e2', 's1', 's2',]
