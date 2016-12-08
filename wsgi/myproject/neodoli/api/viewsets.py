from rest_framework import viewsets
from rest_framework import filters

from neodoli.models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.order_by('name')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)

	search_fields = ('name', 'city', 'address', 'email',)


class PharmacyViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='ph')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)

	search_fields = ('name', 'city', 'address', 'email',)


class ClinicViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='cli')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)

	search_fields = ('name', 'city', 'address', 'email',)


class LaboratoryViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='lab')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)
	
	search_fields = ('name', 'city', 'address', 'email',)