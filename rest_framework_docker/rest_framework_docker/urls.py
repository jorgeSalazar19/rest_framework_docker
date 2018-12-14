from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from apis.viewsets.countryViewset import (
	 CountryList,
	 CountryDetail,
	 CountryUpdate,
	 CountryDestroy,
	 CountryCreate
)


urlpatterns = [
	path('countries/list/', CountryList.as_view()),
	path('country/<int:pk>/detail/', CountryDetail.as_view()),
	path('country/<int:pk>/update/', CountryUpdate.as_view()),
	path('country/<int:pk>/destroy/', CountryDestroy.as_view()),
	path('country/create/', CountryCreate.as_view()),
    path('admin/', admin.site.urls),
]
