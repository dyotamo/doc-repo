from django.db import models
from django.utils import timezone

from .validators import is_timetable

# Create your models here.

cities = [
	('mpt', 'Maputo'),
	('mtl', 'Matola'),
	('xai', 'Xai-Xai'),
	('ibn', 'Inhambane'),
	('btw', 'Beira'),
	('chm', 'Chimoio'),
	('tet', 'Tete'),
	('qlm', 'Quelimane'),
	('npl', 'Nampula'),
	('lcg', 'Lichinga'),
	('pmb', 'Pemba'),
]

class Pharmacy(models.Model):

	""" Pharmacies profile """

	name = models.CharField(max_length=35)
	
	city = models.CharField(max_length=35, choices=cities)
	address = models.CharField(max_length=100)

	tel1 = models.CharField('Telephone 1', max_length=20)
	tel2 = models.CharField('Telephone 2', max_length=20, blank=True, null=True)
	fax = models.CharField(max_length=20, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)

	lat = models.FloatField('Latitude', blank=True, null=True)
	lng = models.FloatField('Longitude', blank=True, null=True)

	timetable = models.CharField(max_length=50, validators=[is_timetable,])

	def __str__(self):
		return self.name

	def working(self):
		now = str(timezone.now().hour)
		points = self.timetable.split(', ')

		if (now > points[0] and now < points[1] or now > points[2] and now < points[3]):
			return True
		else:
			return False
		