from django.urls import path
from . import admincontroller

app_name = 'Admin'
urlpatterns = [
    path("", admincontroller.listProduct, name='Admin'),
    path("addproduct/", admincontroller.addProduct , name='addproduct'),
    path("addcategory/", admincontroller.addCategory , name='addcategory'),
    path("listproduct/", admincontroller.listProduct , name='listproduct'),
    path("listcategory/", admincontroller.listCategory , name='listcategory'),
    path("staffaccounts/",admincontroller.staffAccount , name='staffaccounts'),
    path("customeraccounts/",admincontroller.customerAccount , name='customeraccounts'),
    path("liststaffsales/",admincontroller.listStaffSales , name='liststaffsales'),
    path("revenue/",admincontroller.revenue , name='revenue'),
    path("createaccount/",admincontroller.createAccount , name='createaccount'),
    path("updateproduct/<str:id>/",admincontroller.updateProduct , name='updateproduct'),
    path("updatestaff/<str:id>/",admincontroller.updateStaff , name='updatestaff'),
    path("deleteproduct/<str:id>/",admincontroller.delProduct , name='delproduct'),
    path("deletecategory/<str:id>/",admincontroller.delCategory,name="deletecategory")
    
]
