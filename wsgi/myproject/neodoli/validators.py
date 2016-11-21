from django.core.exceptions import ValidationError

def is_timetable(value):
	points = value.split(', ')

	if len(points) != 4:
		raise ValidationError('%s is invalid' % value)

	for x in points:
		try:
			int(x)
		except ValueError:
			raise ValidationError('%s is invalid' % value)			