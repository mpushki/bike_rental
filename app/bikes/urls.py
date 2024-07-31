from django.urls import path
from bikes.views import BikeListAPIView, AvailableBikeListAPIView

urlpatterns = [
    path(
        'bikes/',
        BikeListAPIView.as_view(),
        name='bike_list',
    ),
    path(
        'available/',
        AvailableBikeListAPIView.as_view(),
        name='available_bikes_list',
    ),
]
