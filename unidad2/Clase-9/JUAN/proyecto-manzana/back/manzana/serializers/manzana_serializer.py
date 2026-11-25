from rest_framework import serializers

from ..models import Manzana


class ManzanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzana
        fields = ["id", "forma", "tamano", "peso_g", "color_cascara"]
        extra_kwargs = {
            "forma": {"label": "Forma", "help_text": "redonda, ovalada, conica o achatada."},
            "tamano": {"label": "Tamaño", "help_text": "pequeno, mediano o grande."},
            "peso_g": {"label": "Peso (g)", "help_text": "Mayor que 0 y hasta 1000. Ejemplo: 180.50"},
            "color_cascara": {"label": "Color de la cáscara", "help_text": "roja, verde, amarilla o bicolor."},
        }

    def validate_peso_g(self, valor):
        if valor <= 0:
            raise serializers.ValidationError("El peso debe ser mayor que cero.")
        if valor > 1000:
            raise serializers.ValidationError("Una manzana no puede pesar más de 1000 g.")
        return valor
