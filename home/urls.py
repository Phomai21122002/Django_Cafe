from django.urls import path
from . import views
app_name = 'Home'
urlpatterns = [
    path("", views.index, name = 'Home' ),
    path("Introduce/", views.Introduce, name = 'Introduce' ),
    path("Product/<str:id>/", views.Product, name = 'Product'),
    path("News/", views.News, name = 'News' ),
    path("Menu/", views.Menu, name = 'Menu' ),
    path("Contact/", views.Contact, name = 'Contact' ),
    path("Login/", views.Login, name='Login'),
    path("Register/", views.Register, name='Register'),
    path("Detail-Product/<str:id>/", views.Detail_Product, name='Detail-Product'),
    path("Cart-Product", views.Cart_Product, name='Cart-Product'),
]
