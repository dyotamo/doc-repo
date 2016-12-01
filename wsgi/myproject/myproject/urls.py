from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^', include('neodoli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jet/', include('jet.urls', 'jet')),
    
    # Deve coincidir com o MEDIA_URL
    url(r'^uploads/', include('mediaserver.urls')),
]