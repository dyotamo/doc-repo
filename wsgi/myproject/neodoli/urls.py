from django.conf.urls import include, url

from .views import Home

urlpatterns = [
	url(r'^$', Home.as_view(), name='homepage'),
    url(r'^api/', include('neodoli.api.urls')),
]
