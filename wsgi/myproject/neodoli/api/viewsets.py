from rest_framework import viewsets

from neodoli.models import Pharmacy
from .serializers import PharmacySerializer

class PharmacyViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Pharmacy.objects.all()
	serializer_class = PharmacySerializer
	# search_fields = ('id', 'name', 'city', 'address',)