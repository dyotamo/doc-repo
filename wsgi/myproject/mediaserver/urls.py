from django.conf.urls import url

from .views import serve

urlpatterns = [
	url(r'^(.+)$', serve, name='serve-media'),
]
