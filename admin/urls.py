from django.urls import path
from . import admincontroller
from PythonWeb.middleware import LoginRequiredMiddleware

app_name = 'Admin'
urlpatterns = [
    path("", admincontroller.listProduct, name='Admin'),
    path("addproduct/", admincontroller.addProduct , name='addproduct'),
    path("addcategory/", admincontroller.addCategory , name='addcategory'),
    path("listproduct/", admincontroller.listProduct , name='listproduct'),
    path("listproductbycategory/<str:id>/", admincontroller.listProduct_by_Category , name='listproductbycategory'),
    path("listcategory/", admincontroller.listCategory , name='listcategory'),
    path("staffaccounts/",admincontroller.staffAccount , name='staffaccounts'),
    path("customeraccounts/",admincontroller.customerAccount , name='customeraccounts'),
    path("liststaffsales/",admincontroller.listStaffSales , name='liststaffsales'),
    path("revenue/",admincontroller.revenue , name='revenue'),
    path("createaccount/",admincontroller.createAccount , name='createaccount'),
    path("updateproduct/<str:id>/",admincontroller.updateProduct , name='updateproduct'),
    path("updateCategory/<str:id>/",admincontroller.updateCategory , name='updateCategory'),
    path("updatestaff/<str:id>/",admincontroller.updateStaff , name='updatestaff'),
    path("resetpass/<str:id>/",admincontroller.resetPass , name='resetpass'),
    path("deleteproduct/<str:id>/",admincontroller.delProduct , name='delproduct'),
    path("deletecategory/<str:id>/",admincontroller.delCategory , name='delcategory'),
    path("deletestaff/<str:id>/",admincontroller.delStaff , name='delstaff'),
    path("logout/",admincontroller.Logout , name='logout'),
    path("updateprofile/",admincontroller.UpdateProfile,name='updateprofile'),
    path("updatepassword/",admincontroller.UpdatePassword , name='updatepass'),
    path("profile/",admincontroller.Profile , name='profile'),
    path("changepassword/",admincontroller.ChangePassWord , name='password'),
    path("updatesales/<str:id>/",admincontroller.updateSales , name='updatesales'),
    path("viewdetailenvenue/<str:id>/",admincontroller.detailEnvenue , name='viewdetailenvenue'),
    path("viewdetailbill/<str:id>/",admincontroller.viewdetailbill , name='viewdetailbill'),
]
