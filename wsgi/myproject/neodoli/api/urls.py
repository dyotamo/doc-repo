from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from .viewsets import PharmacyViewSet

router = routers.SimpleRouter()
router.register(r'pharmacies', PharmacyViewSet)

urlpatterns = router.urls # + [url(r'^token-auth/$', views.obtain_auth_token),]

