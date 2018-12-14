from django.db import models


class Country(models.Model):
	"""Country Management Model

	Attributes:
		name_country: country's name
		country_code: code of country (use for application)

	"""
	name = models.CharField('Name', max_length=100)
	code = models.CharField('Code', max_length=3)

	class Meta:
		verbose_name = "Country"
		verbose_name_plural = "Countries"

	def __str__(self):
		return '{} {}'.format(self.name, self.code)
