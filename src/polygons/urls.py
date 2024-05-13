from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('add', views.Add.as_view(), name="add"),
    path('create', views.Create.as_view(), name="create"),
]
