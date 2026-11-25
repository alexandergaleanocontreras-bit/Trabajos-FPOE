from rest_framework import viewsets

from ..models import Manzana
from ..serializers import ManzanaSerializer


class ManzanaViewSet(viewsets.ModelViewSet):
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer
