from rest_framework import viewsets
from academico.models.gorra import Gorra
from academico.serializers.gorra_serializer import GorraSerializer

class GorraViewSet(viewsets.ModelViewSet):
    queryset = Gorra.objects.all()
    serializer_class = GorraSerializer