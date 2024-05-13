from django.contrib import messages
from django.contrib.gis.geos import Polygon, GEOSException
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import models
from .utils import PolygonUtils


class Add(generic.View):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self._post = request.POST
        self._sess_form_data = request.session.get('_form_data')
        self._get_coord()
        self._get_polygon()

    def post(self, *args, **kwargs):
        self.request.session['_form_data'] = {'name': self._post.get('name'), 'polygon': self._polygon}
        return redirect(reverse_lazy('index'))

    def _get_polygon(self):
        self._polygon = [*self._sess_form_data.get('polygon'), self._coord] if self._sess_form_data else [self._coord]

    def _get_coord(self):
        self._coord = [float(self._post.get('latitude')), float(self._post.get('longitude'))]


class Create(generic.View):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self._sess_form_data = request.session.get('_form_data')
        self._polygon_data = self._sess_form_data.get('polygon')
        self._is_polygon = False

        self._get_polygon()

        if self._is_polygon:
            self._get_model_data()
            self._save()
            del self.request.session['_form_data']

    def get(self, *args, **kwargs):
        return redirect(reverse_lazy('index'))

    def _get_model_data(self):
        name = self._sess_form_data.get('name')
        self._model_data = {'name': name, 'polygon': self._polygon, 'crosses_antimeridian': self._crosses_antimeridian}

    def _get_polygon(self):
        try:
            self._polygon = Polygon(self._polygon_data)
            self._crosses_antimeridian = PolygonUtils.check_crosses_antimeridian(self._polygon_data)
            self._is_polygon = True
        except ValueError:
            messages.error(self.request, 'Размер полигона должен составлять не менее 4-х точек (координат), '
                                         f'и оканчиваться он должен на начальную точку (координату) {self._polygon_data[0]}')
        except GEOSException:
            messages.error(self.request, 'Возникла ошибка при проверке геометрии, возможно вы забыли замкнуть фигуру, '
                                         f'на начальную точку (координату) {self._polygon_data[0]}')

    def _save(self):
        obj = models.PolygonCoord(**self._model_data)
        obj.save()


class Index(generic.ListView):
    model = models.PolygonCoord
    template_name = "polygons/index.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.AddForm(initial=self._get_form_initial())
        return context

    def _get_form_initial(self):
        sess_form_data = self.request.session.get('_form_data')
        if not sess_form_data:
            return []
        _name = sess_form_data.get('name')
        return {'name': _name, 'polygon': f"{_name}\n{sess_form_data.get('polygon')}"}
