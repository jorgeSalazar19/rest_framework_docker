from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from apis.viewsets.countryViewset import CountryList, CountryDetail

schema_view = get_schema_view(title='countries API')

urlpatterns = [
	path(r'schema/', schema_view),
	path('countries/list/', CountryList.as_view()),
	path('countries/detail/<int:pk>', CountryDetail.as_view()),
    path('admin/', admin.site.urls),
]
