import re
from django.core.exceptions import ValidationError

def validate_timetable(value):
	if re.match(r'\d\d?, \d\d?, \d\d?, \d\d?', value):
		points = value.split(', ')

		if int(points[0]) >= 0 and int(points[0]) < int(points[1]) and int(points[1]) <= int(points[2]) and int(points[2]) < int(points[3]) and int(points[3]) < 24:
			pass
		else:
			raise ValidationError('%s is not valid' % value)
	else:
		raise ValidationError('%s is not valid' % value)