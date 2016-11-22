from rest_framework import viewsets
from rest_framework import filters

from neodoli.models import Pharmacy
from .serializers import PharmacySerializer

class PharmacyViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Pharmacy.objects.all()
	serializer_class = PharmacySerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'city', 'address', 'email',)