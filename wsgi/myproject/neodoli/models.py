from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Place(models.Model):

	""" Pharmacies, Clinics and Labs profile """

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

	name 		= models.CharField(max_length=35)
	
	city 		= models.CharField(max_length=35, choices=cities)
	address 	= models.CharField(max_length=100)

	tel1 		= models.CharField('Telephone 1', max_length=20)
	tel2 		= models.CharField('Telephone 2', max_length=20, blank=True, null=True)
	fax 		= models.CharField(max_length=20, blank=True, null=True)
	email 		= models.EmailField(max_length=50, blank=True, null=True)

	lat 		= models.FloatField('Latitude', blank=True, null=True)
	lng 		= models.FloatField('Longitude', blank=True, null=True)

	category 	= models.CharField(max_length=3, choices=categories)
	image 		= models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)

	# Timetable
	e1			= models.PositiveIntegerField('Primeira entrada', default=8)
	s1			= models.PositiveIntegerField('Primeira saída', default=12)

	e2			= models.PositiveIntegerField('Segunda entrada', default=14)
	s2			= models.PositiveIntegerField('Segunda saída', default=18)

	def is_24h(self):
		return (self.e1 == 0) and (self.s1 == self.e2) and (self.s2 == 23)

	def is_working(self):
		if self.is_24h():
			return True
		
		# Se for sábado, funciona apenas em meio termo ...
		now = timezone.now()

		if now.isoweekday() == 6:
			# Então verifica se a hora atual
			# é maior ou igual a entrada e 
			# menor que a saída
			return self.e1 <= now.hour < self.s1
		# Se for domingo, verifica 
		elif now.isoweekday() == 7:
			return False

		return (self.e1 <= now.hour < self.s1) or (self.e2 <= now.hour < self.s2)
	is_working.boolean = True

	def __str__(self):
		return self.name

	def clean(self, *args, **kwargs):
		# Ex: (8 - 12; 14 - 20) e não (8 - 7; 0 - 9)
		if 0 <= self.e1 < self.s1 <= self.e2 < self.s2 <= 23:
			return super(Place, self).clean(*args, **kwargs)
		
		raise ValidationError('O horário de funcionamento não está correto.')
