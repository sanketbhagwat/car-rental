from rest_framework import serializers
from .models import vehicles

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicles
        fields=['id','Category']