from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("Introduce/", views.Introduce),
    path("Product/", views.Product),
    path("News/", views.News),
    path("Menu/", views.Menu),
    path("Contact/", views.Contact),
    path("Login/", views.Login),
    path("Register/", views.Register),
]
