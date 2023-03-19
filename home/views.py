from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin import admincontroller
from . import models

def index(request):
    return render(request, 'pages/home.html')

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
                return redirect('Admin')
            else:
                return HttpResponse('Email or PassWord is not accept')        
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

        return redirect('Login')

    return render(request, 'pages/Register.html')
# Create your views here.
