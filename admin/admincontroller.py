
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def addProduct(request):
    return render(request,'pages/addProduct.html')

def staffAccount(request):
    return render(request,'pages/listStaffAccount.html')


def createAccount(request):
    return render(request,'pages/createAccount.html')

def customerAccount(request):
    return render(request,'pages/listCustomerAccount.html')
