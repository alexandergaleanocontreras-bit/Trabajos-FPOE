from rest_framework import viewsets

from manzana.models import Manzana
from manzana.serializers import ManzanaSerializer


class ManzanaViewSet(viewsets.ModelViewSet):
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer