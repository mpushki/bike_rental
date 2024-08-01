from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        read_only_fields = ("id",)
        fields = ('id', 'tenant', 'bike', 'started_at', 'finished_at', 'worth')
