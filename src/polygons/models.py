from django.contrib.gis.db import models


class PolygonCoord(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    polygon = models.PolygonField(srid=3857, verbose_name='Список координат')
    crosses_antimeridian = models.BooleanField(default=False, verbose_name='Признак пересечения антимеридиана')

    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Полигон (местоположения)'
        verbose_name_plural = 'Полигоны (местоположения)'

    def __str__(self):
        return self.name

