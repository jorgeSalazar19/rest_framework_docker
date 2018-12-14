from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
