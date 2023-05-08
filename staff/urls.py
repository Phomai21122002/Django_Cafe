from django.urls import path
from . import views

app_name = 'Staff'
urlpatterns = [
    path("", views.index, name='Staff'),
    path("addproduct/", views.addProduct , name='addproduct'),
    path("addcategory/", views.addCategory , name='addcategory'),
    path("listproduct/", views.listProduct , name='listproduct'),
    path("listproductbycategory/<str:id>/", views.listProduct_by_Category , name='listproductbycategory'),
    path("listcategory/", views.listCategory , name='listcategory'),
    path("staffaccounts/",views.staffAccount , name='staffaccounts'),
    path("customeraccounts/",views.customerAccount , name='customeraccounts'),
    path("liststaffsales/",views.listStaffSales , name='liststaffsales'),
    path("revenue/",views.revenue , name='revenue'),
    path("createaccount/",views.createAccount , name='createaccount'),
    path("updateproduct/<str:id>/",views.updateProduct , name='updateproduct'),
    path("updateCategory/<str:id>/",views.updateCategory , name='updateCategory'),
    path("updatestaff/<str:id>/",views.updateStaff , name='updatestaff'),
    path("deleteproduct/<str:id>/",views.delProduct , name='delproduct'),
    path("deletecategory/<str:id>/",views.delCategory , name='delcategory'),
    path("logout/",views.Logout , name='logout'),
    path("profile/",views.Profile , name='profile'),
    path("changepassword/",views.ChangePassWord , name='password'),
    path("updatesales/<str:id>/",views.updateSales , name='updatesales'),
    path("viewdetailbill/<str:id>/",views.viewdetailbill , name='viewdetailbill'),
]
