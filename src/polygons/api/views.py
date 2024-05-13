from rest_framework import viewsets

from .. import models
from . import serializers


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = models.PolygonCoord.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.GetPolygonSerializer
        elif self.action == 'list':
            return serializers.GetPolygonSerializer
        elif self.action == 'update':
            return serializers.UpdatePolygonSerializer
        elif self.action == 'partial_update':
            return serializers.UpdatePolygonSerializer
        elif self.action == 'create':
            return serializers.CreatePolygonSerializer
