from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response

from neodoli.models import Place
from .serializers import PlaceSerializer


fields = ('name', 'city',
			'address', 'email',)

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.order_by('name')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)
	search_fields = fields

	def list(self, request):
		try:
			# If KeyError, to default ...
			all = request.GET['all']
			queryset = Place.objects.order_by('name')
			serializer = PlaceSerializer(queryset,
											many=True)

			return Response(serializer.data)
		except:
			return super(PlaceViewSet,
							self).list(request)


class PharmacyViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='ph')
	serializer_class = PlaceSerializer

	filter_fields = fields
	search_fields = ('name', 'city', 'address', 'email',)


class ClinicViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='cli')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)
	search_fields = fields


class LaboratoryViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='lab')
	serializer_class = PlaceSerializer

	filter_fields = ('city',)
	search_fields = fields