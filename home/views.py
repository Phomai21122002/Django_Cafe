from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
import json
from django.http import JsonResponse

def index(request):
    result = models.listcategory()
    for i in result:
        if( i.Name_Category == 'Cafe'):
            id_product = i.id
    result_product = models.get_product_by_category_id(id_product)
    product_order = models.get_different_product(id_product)

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
        Number_Phone = request.POST['numberPhone']  
        Address = request.POST['Address']  
        models.handle_order(carts, Number_Phone, Address)
        data = {
            'result': True,
        }
        return JsonResponse(data)

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
            'Picture': product.Url_Image,
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
        checkLogin, classify = models.Login(Email, PassWord)
        print(Email, PassWord)
        print(checkLogin.id)
        print(classify)
        if(classify == "1" and Email == checkLogin.Email and PassWord == checkLogin.Pass_Word):
            print(checkLogin)
            request.session['id'] = checkLogin.id
            request.session['classify'] = checkLogin.Classify
            data = {
                'id': checkLogin.id,
                'classify': checkLogin.Classify,
            }
            return JsonResponse(data) 
        elif(classify == "2" and Email == checkLogin.Email and PassWord == checkLogin.Pass_Word):
            print('nhan vien',checkLogin)
            request.session['id'] = checkLogin.id
            request.session['classify'] = checkLogin.Classify
            data = {
                'id': checkLogin.id,
                'classify': checkLogin.Classify,
            }
            return JsonResponse(data)
        elif(checkLogin == False):
            print('error email')
            data = {
                'result': True,
            }
            return JsonResponse(data)
        elif(Email == checkLogin.Email and PassWord != checkLogin.Pass_Word):
            print('error pass')
            data = {
                'result': False,
            }
            return JsonResponse(data)
        elif(checkLogin == 0 and classify == 0):
            print('error')
            data = {
                'result': 0,
            }
            return JsonResponse(data)

    return render(request, 'pages/Login.html')

def Register(request):

    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        Date = request.POST['datetime']
        
        models.Register(FirstName, Email, password, numberphone, '2', LastName, Date)

        return redirect("Home:Login")

    return render(request, 'pages/Register.html')


# Create your views here.
