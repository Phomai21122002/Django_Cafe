from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'pages/Login.html')

def Register(request):
    return render(request, 'pages/Register.html')
# Create your views here.
