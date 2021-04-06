import django_filters

from .models import vehicles

class vehicleFilter(django_filters.FilterSet):
	class Meta:
		model = vehicles