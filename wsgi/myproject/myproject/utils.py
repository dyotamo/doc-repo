import mimetypes
import os

from django.http import HttpResponse, Http404
from django.conf import settings

def serve(request, path):
	response = HttpResponse()
	absolute_name = os.path.join(settings.DATA_DIR, path)

	try:
		with open(absolute_name, 'rb') as file:
			for chuck in file:
				response.write(chuck)
	except IOError:
		raise Http404

	response['Content-type'] = mimetypes.guess_type(absolute_name)[0]
	return response

