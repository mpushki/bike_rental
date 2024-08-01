from django.core.exceptions import ValidationError, PermissionDenied
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone


class OrderCreateAPIView(generics.CreateAPIView):
    '''
    Bicycle rental order.
    User is added automatically from authentication data
    User can rent only 1 bike
    Bike cannot be rented again
    '''
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        has_actual_order = Order.objects.filter(tenant=self.request.user, finished_at__isnull=True).exists()
        if has_actual_order:
            raise PermissionDenied("You cannot rent more then 1 bike.")

        bike = serializer.validated_data.get('bike')
        if bike.rent_is:
            raise ValidationError("This bike is not available.")

        bike.in_rent = True
        bike.save()

        serializer.save(tenant=self.request.user)


class ReturnBikeAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):

        bike = serializer.validated_data.get('bike')

        bike.rent_is = False
        bike.save()
        serializer.save(finished_at=timezone.now())


class OrderHistoryAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(tenant=self.request.user)
