from django.urls import path
from . import admincontroller

app_name = 'Admin'
urlpatterns = [
    path("", admincontroller.index, name='Admin'),
]
