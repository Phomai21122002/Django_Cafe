
from django.shortcuts import render, redirect
from home.models import *
from django.http import JsonResponse
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

def listProduct_by_Category(request, id):
    products = get_product_by_category_id(id)

    context = {'products': products}
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
        return redirect('Admin:listcategory')
    context = {"Category": Category}
    return render(request, 'pages/updateCategory.html', context)

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
    deleteProduct_Order(id)
    deleteProduct(id)
    return redirect('Admin:listproduct')

def delCategory(request, id):
    deleteCategory(id)
    return redirect('Admin:listcategory')

def revenue(request):
    result_orderDetail, result_order = revenue_product(2)
    context = {"result_orderDetail": result_orderDetail, "result_order": result_order}
    return render(request, 'pages/listRevenue.html')

def Logout(request):
    del request.session['id']
    return redirect('Home:Home')

def Profile(request):
    idUser = request.session.get('id')
    myProfile = getUserByID(idUser)
    context = {"user": myProfile}
    return render(request, 'pages/profile.html', context)
    
def ChangePassWord(request):
    return render(request, 'pages/changepassword.html')
    
def UpdateProfile (request):

    idUser = request.session.get('id')

    if request.method == "POST":
        lastName = request.POST['lastname']
        firsttName = request.POST['firstname']
        numberphone = request.POST['numberphone']
        updateProfile(id=idUser, firstName=firsttName, lastName=lastName, phoneNumber=numberphone)
        return redirect("Admin:profile")

def ResetPassword (request,id):
    resetPass(id)
    return redirect("Admin:staffaccounts")

def UpdatePassword(request):

    idUser = request.session.get('id')

    if request.method == "POST":
        oldPass = request.POST['oldpass']
        newPass = request.POST['newpass']

        print(oldPass)
        print(newPass)
        user = getUserByID(id = idUser)
        if(oldPass == user.Pass_Word):
            updatePass(id=idUser, newPass=newPass)
            data = {
                'result': True,
            }
            return JsonResponse(data)
        else:
            data = {
                'result': False,
            }
            return JsonResponse(data)

        
        
        
    
    
   
    