from rest_framework import serializers

from countries.models import Country



class CountrySerializer(serializers.ModelSerializer):
	"""
	Serializador para le modelo country
	"""

	class Meta:

		model = Country
		fields = ('name', 'code')