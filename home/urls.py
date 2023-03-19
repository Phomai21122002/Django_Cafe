from django.urls import path
from . import views
app_name = 'Home'
urlpatterns = [
    path("", views.index, name = 'Home' ),
    path("Introduce/", views.Introduce, name = 'Introduce' ),
    path("Product/", views.Product, name = 'Product' ),
    path("News/", views.News, name = 'News' ),
    path("Menu/", views.Menu, name = 'Menu' ),
    path("Contact/", views.Contact, name = 'Contact' ),
    path("Login/", views.Login, name='Login'),
    path("Register/", views.Register, name='Register'),
]
