from django.shortcuts import render, redirect
from . import models


def index(request):
    query = "Select * from product where IdCategory = 1"
    datas = models.connect_mysql_get_data(query)
    result = []
    for data in datas:
        result.append({
            'IDProduct': data[0],
            'NameProduct': data[1],
            'url_image': data[5],
        })

    query_order = "Select * from product where IdCategory != 1"
    datas = models.connect_mysql_get_data(query_order)
    result_order = []
    for data in datas:
        result_order.append({
            'IDProduct': data[0],
            'NameProduct': data[1],
            'Price': data[2],
        })

    context = {'products': result, 'product_order': result_order}

    return render(request, 'pages/home.html', context)

def Introduce(request):
    return render(request, 'pages/Introduce.html')

def Product(request):
    return render(request, 'pages/Product.html')

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
        query = 'SELECT * FROM user WHERE Classify = 1'
        result_mysql = models.connect_mysql_get_data(query)
        for data in result_mysql:
            if data[2] == Email and data[3] == PassWord:
                request.session['id'] = data[0]
                request.session['classify'] = data[5]
                return redirect('Admin:Admin')       
    return render(request, 'pages/Login.html')

def Register(request):

    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']
        print(LastName,FirstName,Email,numberphone,password)

        query = "insert into user(FisrtName, Email, Pass_word, Phone_number, Classify, LastName) values('"+ FirstName +"', '"+ Email +"', '"+ password +"', '"+ numberphone +"', 1, '"+ LastName +"')"

        models.connect_mysql(query)

        return redirect("Home:Login")

    return render(request, 'pages/Register.html')
# Create your views here.
