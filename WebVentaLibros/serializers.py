from rest_framework import serializers
from .models import libro


class libroSerializers (serializers.ModelSerializer):
    class Meta:
        model = libro
        fields = '__all__'
