
from django.shortcuts import render, redirect
from home.models import *
import os


def index(request):
    return render(request, 'pages/index.html')

def addProduct(request):
    if request.method == 'POST':
        NameProduct = request.POST['nameproduct']
        Price = request.POST['price']
        Description = request.POST['description']
        Category_id = request.POST['category']
        Image = request.FILES['Image']
    
        addproduct(NameProduct, Price, Description, Image, Category_id)
        return redirect('Admin:listproduct')

    arrayCategory = listcategory()
    context = {'category': arrayCategory}

    return render(request,'pages/addProduct.html', context)

def addCategory(request):
    if request.method == 'POST':
        NameCategory = request.POST['namecategory']
        Image = request.FILES['Image']
        addcategory(NameCategory, Image)

        return redirect('Admin:listcategory')
    return render(request, 'pages/addCategory.html')

def listProduct(request):
    result = listproduct()
    context = {'products': result}
    return render(request, 'pages/listProduct.html', context)

def listCategory(request):
    result = listcategory()
    context = {'categorys': result}
    return render(request, 'pages/listCategory.html', context)

def staffAccount(request):
    result = liststaff()
    context = {'staffs': result}

    return render(request,'pages/listStaffAccount.html', context)

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

        return redirect("Admin:staffaccounts")

    return render(request,'pages/createAccount.html')

def customerAccount(request):
    return render(request,'pages/listCustomerAccount.html')


# adjust
def updateProduct(request, id):
    result = get_product_by_id(id)

    if request.method == 'POST':
        NameProduct = request.POST['nameproduct']
        Price = request.POST['price']
        Description = request.POST['description']
        Category = request.POST['category']
        if len(request.FILES) != 0:
            if len(result.Url_Image) > 0:
                os.remove(result.Url_Image.path)
            Image = request.FILES['Image']
        else:
            Image = result.Url_Image

        updateproduct(id, NameProduct, Price, Description, Image, Category)
        return redirect('Admin:listproduct')

    result_category = listcategory()
    context = {'Product': result, 'listCategory': result_category}
    return render(request, 'pages/updateProduct.html', context)

def updateStaff(request, id):
    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        Date = request.POST['date']
        updatestaff(id, FirstName, Email, password, numberphone, LastName, Date)
        return redirect("Admin:staffaccounts")
    result = get_staff_by_id(id)
    context = {'staff': result}
    return render(request, 'pages/updateStaff.html', context)


def listStaffSales(request):
    result_orderDetail, result_order = sales_product(2)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/listStaffSales.html', context)

def delProduct (request,id):
    deleteProduct(id)
    return redirect('Admin:listproduct')

def revenue(request):
    result_orderDetail, result_order = revenue_product(2)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/listRevenue.html')

def Logout(request):
    del request.session['id']
    return redirect('Home:Home')
