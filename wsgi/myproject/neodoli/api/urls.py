from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import PlaceViewSet, PharmacyViewSet, ClinicViewSet, LaboratoryViewSet

router = routers.SimpleRouter()

router.register(r'places', PlaceViewSet)
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'clinics', ClinicViewSet)
router.register(r'labs', LaboratoryViewSet)

urlpatterns = router.urls

