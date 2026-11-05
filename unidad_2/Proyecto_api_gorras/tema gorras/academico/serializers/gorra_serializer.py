from rest_framework import serializers
from academico.models.gorra import Gorra

class GorraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gorra
        fields = '__all__'