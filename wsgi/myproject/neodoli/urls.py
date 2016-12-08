from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='neodoli/static/about.html')),
    url(r'^api/', include('neodoli.api.urls')),
]
