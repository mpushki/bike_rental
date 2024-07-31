from rest_framework import serializers

from bikes.models import Bike


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        read_only_fields = ("id",)
        fields = ("id", "model", "price")
