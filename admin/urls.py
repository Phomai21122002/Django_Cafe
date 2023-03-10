from django.urls import path
from . import admincontroller

urlpatterns = [
    path("", admincontroller.index),
]
