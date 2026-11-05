from rest_framework import viewsets
from gorras.models.gorra import Gorra
from gorras.serializers.gorra_serializer import GorraSerializer

class GorraViewSet(viewsets.ModelViewSet):
    queryset = Gorra.objects.all()
    serializer_class = GorraSerializer