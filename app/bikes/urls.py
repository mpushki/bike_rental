from django.urls import path
from bikes.views import BikeListAPIView

urlpatterns = [
    path(
        'bikes/',
        BikeListAPIView.as_view(),
        name='bike-list',
    ),
]
