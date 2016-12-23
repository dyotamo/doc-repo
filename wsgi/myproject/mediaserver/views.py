import mimetypes
import os

from django.http import FileResponse, Http404
from django.conf import settings

def serve(request, path):	
	try:
		absolute_name = os.path.join(settings.MEDIA_ROOT, path)
		response = FileResponse(open(absolute_name, 'rb'))
		content_type = mimetypes.guess_type(absolute_name)[0]
		response['Content-Type'] = content_type

		try:
			request.GET['download']
			response['Content-Disposition'] = ('attachment; filename="file.%s"'
												% content_type.split('/')[-1]) # Get file extension ...
		except:
			pass

		return response
	except IOError:
		raise Http404