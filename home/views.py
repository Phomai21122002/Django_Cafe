from django.shortcuts import render, redirect
from . import models


def index(request):
    result = models.listcategory()
    result_product = models.get_product_by_category_id(1)
    product_order = models.get_different_product(1)

    context = {'Categorys': result, 'Products': result_product, 'Product_Order': product_order}
    return render(request, 'pages/home.html', context)

def Introduce(request):
    return render(request, 'pages/Introduce.html')

def Product(request, id):
    result = models.get_product_by_category_id(id)
    context = {"Products": result}
    return render(request, 'pages/Product.html', context)

def Detail_Product(request, id):

    if(request.method == 'POST'):
        print(models.get_product_by_id(id).id, models.get_product_by_id(id).Name_Product)
        return redirect('Home:Cart-Product')
    result = models.get_product_by_id(id)
    result_product_different = models.get_different_product(id)
    context = {'Product': result, 'Products_different': result_product_different}
    return render(request, 'pages/Detail-Product.html', context)

def Cart_Product(request):
    return render(request, 'pages/Cart-Product.html')

def News(request):
    return render(request, 'pages/News.html')

def Menu(request):
    return render(request, 'pages/Menu.html')

def Contact(request):
    return render(request, 'pages/Contact.html')

def Login(request):

    if request.method == "POST":
        Email = request.POST['email']
        PassWord = request.POST['password']
        checkLogin = models.Login(Email, PassWord)

        if checkLogin != 0:
            request.session['id'] = checkLogin.id
            request.session['classify'] = checkLogin.Classify
        return redirect('Admin:Admin')     
    return render(request, 'pages/Login.html')

def Register(request):

    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        Date = request.POST['datetime']
        
        models.Register(FirstName, Email, password, numberphone, 1, LastName, Date)

        return redirect("Home:Login")

    return render(request, 'pages/Register.html')

# Create your views here.
