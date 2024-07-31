from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bikes.models import Bike
from bikes.serializers import BikeSerializer


class BikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    # permission_classes = [IsAuthenticated]

class AvailableBikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.filter(rent_is=False)
    serializer_class = BikeSerializer
    # permission_classes = [IsAuthenticated]
