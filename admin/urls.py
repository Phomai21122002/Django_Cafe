from django.urls import path
from . import admincontroller

app_name = 'Admin'
urlpatterns = [
    path("", admincontroller.index, name='Admin'),
    path("addproduct/", admincontroller.addProduct),
    path("staffaccounts/",admincontroller.staffAccount),
    path("customeraccounts/",admincontroller.customerAccount),
    path("createaccount/",admincontroller.createAccount),
    
]
