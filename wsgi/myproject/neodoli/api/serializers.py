from rest_framework import serializers

from neodoli.models import Pharmacy

class PharmacySerializer(serializers.ModelSerializer):

	""" Pharmacies serializer """

	working = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()

	def get_working(self, obj):
		return obj.working()

	def get_city(self, obj):
		return obj.get_city_display()		

	class Meta:
		model = Pharmacy

	def get_days_since_joined(self, obj):
		return (now() - obj.date_joined).days
