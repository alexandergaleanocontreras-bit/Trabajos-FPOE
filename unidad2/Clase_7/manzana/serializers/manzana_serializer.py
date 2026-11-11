from rest_framework import serializers

from manzana.models import Manzana


class ManzanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzana
        fields = "__all__"

    def validate_peso_g(self, value):
        if value <= 0:
            raise serializers.ValidationError("El peso debe ser mayor que cero.")
        if value > 1000:
            raise serializers.ValidationError("Una manzana no puede pesar más de 1000 g.")
        return value