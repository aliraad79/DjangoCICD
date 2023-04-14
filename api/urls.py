from django.urls import path

from .views import index, greet

urlpatterns = [
    path("", index),
    path("greet/<str:name>/<int:age>/", greet),
]
