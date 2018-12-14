from rest_framework import generics


from countries.models import Country
from apis.serializers.countrySerializer import CountrySerializer



class CountryList(generics.ListAPIView):
    """
    lista de todos los paises
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveAPIView):
    """
    muestra los detalles de un pais reciendo el ID del pais por la URL
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdate(generics.UpdateAPIView):
    """
    Actualiza un objeto determinado por un ID enviado como parametro
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDestroy(generics.DestroyAPIView):
    """
    Elimina un objeto determinado or un Id enviado como parametro
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryCreate(generics.CreateAPIView):
    """
    Crea un objeto con los atributos requeridos en el formulario
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
