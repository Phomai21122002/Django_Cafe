from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
import json

def index(request):
    result = models.listcategory()
    result_product = models.get_product_by_category_id(4)
    product_order = models.get_different_product(4)

    context = {'Categorys': result, 'Products': result_product, 'Product_Order': product_order}
    return render(request, 'pages/home.html', context)

def Introduce(request):
    return render(request, 'pages/Introduce.html')

def Product(request, id):
    result = models.get_product_by_category_id(id)
    for data in result:
        data.Url_Image = str(data.Url_Image).strip("home")
    context = {"Products": result}
    return render(request, 'pages/Product.html', context)

def Detail_Product(request, id):
    if(request.method == 'POST'):
        return redirect('Home:Cart-Product')
    
    result = models.get_product_by_id(id)
    context = {'Product': result}
    return render(request, 'pages/Detail-Product.html', context)

def Cart_Product(request):
    carts = json.loads(request.COOKIES.get('cart'))

    if request.method == 'POST':
        choose = request.POST['choose_order']
        if choose == 'here':
            Number_Phone = request.POST['Number_Phone']  
            Address = request.POST['Address']  
            models.handle_order(carts, Number_Phone, Address)
        elif choose == 'home':
            Number_Phone = request.POST['Number_Phone']  
            Address = request.POST['Address']  
            models.handle_order(carts, Number_Phone, Address)
        return redirect('Home:Cart-Product')

    listCart = []
    total_product = 0
    total_price = 0

    # lay du lieu tu cookies
    for cart in carts:
        product = models.get_product_by_id(cart['idProduct'])
        listCart.append({
            'idProduct': product.id,
            'Name_Product': product.Name_Product,
            'Price': product.Price,
            'count': int(cart['count']),
            'total': int(cart['count'])*product.Price,
        })
        total_product += int(cart['count'])
        total_price +=  int(cart['count'])*product.Price

    context = {'carts': listCart, 'total_product': total_product, 'total_price': total_price}
    return render(request, 'pages/Cart-Product.html', context)

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

        if checkLogin:
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
