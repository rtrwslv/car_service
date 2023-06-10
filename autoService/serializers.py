from rest_framework import serializers
from models import Car, Owner, Repair


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = 'all'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = 'all'


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = 'all'
