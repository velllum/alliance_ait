from rest_framework import serializers

from .. import models
from ..utils import PolygonUtils


class BasePolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PolygonCoord
        fields = ['name', 'polygon']

    def to_representation(self, instance):
        antimeridian = PolygonUtils.check_crosses_antimeridian(instance.polygon.coords[0])
        if antimeridian:
            instance.crosses_antimeridian = antimeridian
            instance.save()
        return super().to_representation(instance)


class GetPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PolygonCoord
        fields = ['id', 'name', 'polygon', 'crosses_antimeridian', 'created_date', 'updated_date']


class CreatePolygonSerializer(BasePolygonSerializer):
    class Meta(BasePolygonSerializer.Meta):
        model = models.PolygonCoord


class UpdatePolygonSerializer(serializers.ModelSerializer):
    class Meta(BasePolygonSerializer.Meta):
        model = models.PolygonCoord

