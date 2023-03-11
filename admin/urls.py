from django.urls import path
from . import admincontroller

urlpatterns = [
    path("", admincontroller.index),
    path("addproduct/", admincontroller.addProduct),
    path("staffaccounts/",admincontroller.staffAccount),
    path("customeraccounts/",admincontroller.customerAccount),
    path("createaccount/",admincontroller.createAccount),
    
]
