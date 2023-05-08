
from django.shortcuts import render, redirect
from home.models import *
import os


def index(request):
    return render(request, 'pages/indexStaff.html')

def addProduct(request):
    if request.method == 'POST':
        NameProduct = request.POST['nameproduct']
        Price = request.POST['price']
        Description = request.POST['description']
        Category_id = request.POST['category']
        Image = request.FILES['Image']
    
        addproduct(NameProduct, Price, Description, Image, Category_id)
        return redirect('Staff:listproduct')

    arrayCategory = listcategory()
    context = {'category': arrayCategory}

    return render(request,'pages/addProduct_Staff.html', context)

def addCategory(request):
    if request.method == 'POST':
        NameCategory = request.POST['namecategory']
        Image = request.FILES['Image']
        addcategory(NameCategory, Image)

        return redirect('Staff:listcategory')
    return render(request, 'pages/addCategory_Staff.html')

def listProduct(request):
    result = listproduct()
    context = {'products': result}
    return render(request, 'pages/listProduct_Staff.html', context)

def listProduct_by_Category(request, id):
    products = get_product_by_category_id(id)

    context = {'products': products}
    return render(request, 'pages/listProduct_Staff.html', context)

def listCategory(request):
    result = listcategory()
    context = {'categorys': result}
    return render(request, 'pages/listCategory_Staff.html', context)

def staffAccount(request):
    result = liststaff()
    context = {'staffs': result}

    return render(request,'pages/listStaffAccount_Staff.html', context)

def createAccount(request):
    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        classify = request.POST['classify']
        date = request.POST['date']

        Register(FirstName, Email, password, numberphone, classify, LastName, date)

        return redirect("Staff:staffaccounts")

    return render(request,'pages/createAccount_Staff.html')

def customerAccount(request):
    return render(request,'pages/listCustomerAccount_Staff.html')


# adjust
def updateProduct(request, id):
    result = get_product_by_id(id)

    if request.method == 'POST':
        return redirect('Staff:listproduct')

    result_category = listcategory()
    context = {'Product': result, 'listCategory': result_category}
    return render(request, 'pages/updateProduct_Staff.html', context)

def updateCategory(request, id):
    Category = get_category_by_id(id)

    if request.method == 'POST':
        NameCategory = request.POST['nameCategory']
        if len(request.FILES) != 0:
            if len(Category.Url_Image) > 0:
                os.remove(Category.Url_Image.path)
            Image = request.FILES['Image']
        else:
            Image = Category.Url_Image

        update_category(id, NameCategory, Image)
        return redirect('Staff:listcategory')
    context = {"Category": Category}
    return render(request, 'pages/updateCategory_Staff.html', context)

def updateStaff(request, id):
    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        Date = request.POST['date']
        updatestaff(id, FirstName, Email, password, numberphone, LastName, Date)
        return redirect("Staff:staffaccounts")
    result = get_staff_by_id(id)
    context = {'staff': result}
    return render(request, 'pages/updateStaff_Staff.html', context)

def updateSales(request, id):

    if request.method == 'POST':
        Condition = request.POST['Conditions']
        if Condition == "1":
            if request.session.get('classify') == "2":
                update_sales(id, request.session.get('id'))
            else:
                update_sales(id, request.session.get('id'))
        return redirect('Staff:liststaffsales')

    result_orderDetail, result_order, result_user = sales_product_by_id(id)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order, "result_user": result_user}
    return render(request, 'pages/updateSales_Staff.html', context)

def viewdetailbill(request, id):
    result_orderDetail, result_order = sales_product_by_id(id)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/viewDetailBill_Staff.html', context)

def listStaffSales(request):
    result_orderDetail, result_order = sales_product(2)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/listStaffSales_Staff.html', context)

def delProduct (request,id):
    deleteProduct_Order(id)
    deleteProduct(id)
    return redirect('Staff:listproduct')

def delCategory(request, id):
    deleteCategory(id)
    return redirect('Staff:listcategory')

def revenue(request):
    result_orderDetail, result_order = revenue_product(1)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/listRevenue_Staff.html', context)

def Logout(request):
    del request.session['id']
    return redirect('Home:Home')

def Profile(request):
    return render(request, 'pages/profile_Staff.html')
    
def ChangePassWord(request):
    return render(request, 'pages/changepassword_Staff.html')
    
