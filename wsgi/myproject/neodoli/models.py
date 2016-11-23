from django.db import models
from django.utils import timezone

from .validators import validate_timetable

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

categories = [
	('ph', 'Farmácia'),
	('cli', 'Clínica'),
	('lab', 'Laboratório'),
]

class Place(models.Model):

	""" Pharmacies, Clinics and Labs profile """

	name = models.CharField(max_length=35)
	
	city = models.CharField(max_length=35, choices=cities)
	address = models.CharField(max_length=100)

	tel1 = models.CharField('Telephone 1', max_length=20)
	tel2 = models.CharField('Telephone 2', max_length=20, blank=True, null=True)
	fax = models.CharField(max_length=20, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)

	lat = models.FloatField('Latitude', blank=True, null=True)
	lng = models.FloatField('Longitude', blank=True, null=True)

	timetable = models.CharField(max_length=50, validators=[validate_timetable,])

	def working(self):
		now = timezone.now().hour
		points = self.timetable.split(', ')

		if now >= int(points[0]) and now < int(points[1]) or now >= int(points[2]) and now < int(points[3]):
			return True
		else:
			return False
	working.boolean = True

	category = models.CharField(max_length=3, choices=categories)
	image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)

	def __str__(self):
		return self.name


# Not necessary for this app
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
"""		