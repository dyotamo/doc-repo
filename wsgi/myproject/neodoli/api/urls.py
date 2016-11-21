from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import PharmacyViewSet

router = routers.SimpleRouter()
router.register(r'pharmacies', PharmacyViewSet)

urlpatterns = router.urls

