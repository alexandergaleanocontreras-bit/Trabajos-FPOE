from rest_framework import serializers
from gorras.models.gorra import Gorra

class GorraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gorra
        fields = '__all__'