# rest_framework_docker
Primera parte de prueba tecnica para IKATECH SOLUTIONS

1. Se requiere crear un sistema usando Docker que realice lo siguiente:  crear, modificar, eliminar, listar y ver el detalle por id de registro, usando Django REST framework (http://www.django-rest-framework.org/), usando python 3.5, orientando el codigo a vistas basadas en clases para el siguiente modelo:
	
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
