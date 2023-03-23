
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import connect_mysql_get_data
from home.models import connect_mysql
from home.models import listCategory
import shutil
import os



def index(request):
    return render(request, 'pages/index.html')

def addProduct(request):
    if request.method == 'POST':
        NameProduct = request.POST['nameproduct']
        Price = request.POST['price']
        Description = request.POST['description']
        Category = request.POST['category']
        Image = request.POST['Image']
        
        path = 'E:\Pictures'+ str('\\' + Image)
        os.chmod('home/static/img/', 0o777)
        shutil.copy(path, 'home/static/img/')

        query = "insert into product(NameProduct, Price, Description, IdCategory, url_image) values('" + NameProduct + "', '" + Price + "', '" + Description + "', '" + Category + "', '" + Image + "')"
        connect_mysql(query)
        return redirect('Admin:listproduct')

    query = "Select * from category"
    category = connect_mysql_get_data(query)
    arrayCategory = []
    for data in category:
        arrayCategory.append({
            'id': data[0],
            'NameCategory': data[1],
        })
    content = {'category': arrayCategory}

    return render(request,'pages/addProduct.html', content)

def addCategory(request):
    if request.method == 'POST':
        NameCategory = request.POST['namecategory']
        query = "Insert into category(NameCategory) values('"+ NameCategory +"')"
        connect_mysql(query)

        return redirect('Admin:listcategory')
    return render(request, 'pages/addCategory.html')

def listProduct(request):
    query = "Select * from product"
    result_List_Produce = connect_mysql_get_data(query)
    result = []
    for data in result_List_Produce:
        query_id = "Select NameCategory from category where IdCategory = '"+ str(data[4]) +"'"
        IdCategory = connect_mysql_get_data(query_id)
        result.append({
            'IdProduct': data[0],
            'NameProduct': data[1],
            'Price': data[2],
            'Description': data[3],
            'NameCategory': IdCategory[0][0],
        })

        context = {'products': result}

    return render(request, 'pages/listProduct.html', context)

def listCategory(request):
    query = "Select * from category"
    result_list_category = connect_mysql_get_data(query)
    result = []
    for data in result_list_category:
        result.append({
            'IdCategory': data[0],
            'NameCategory': data[1],
        })
    context = {'categorys': result}
    return render(request, 'pages/listCategory.html', context)

def staffAccount(request):

    query = "Select * from user where Classify=1"
    result_staff = connect_mysql_get_data(query)
    result = []
    for data in result_staff:
        result.append({
            'ID': data[0],
            'FisrtName': data[1],
            'Email': data[2],
            'PassWord': data[3],
            'PhoneNumber': data[4],
            'LastName': data[6],
        })
    context = {'staffs': result}

    return render(request,'pages/listStaffAccount.html', context)

def createAccount(request):
    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']

        query = "insert into user(FisrtName, Email, Pass_word, Phone_number, Classify, LastName) values('"+ FirstName +"', '"+ Email +"', '"+ password +"', '"+ numberphone +"', 1, '"+ LastName +"')"

        connect_mysql(query)

        return redirect("Admin:staffaccounts")

    return render(request,'pages/createAccount.html')

def customerAccount(request):
    return render(request,'pages/listCustomerAccount.html')


# adjust
def updateProduct(request, id):

    if request.method == 'POST':
        NameProduct = request.POST['nameproduct']
        Price = request.POST['price']
        Description = request.POST['description']
        Category = request.POST['category']

        query = "UPDATE `product` SET `NameProduct`='"+ NameProduct +"',`Price`='"+ Price+"',`Description`='"+ Description +"',`IdCategory`='"+ Category +"' WHERE `IdProduct`= '"+ str(id) +"'"
        connect_mysql(query)
        return redirect('Admin:listproduct')

    query = "Select * from product where IdProduct='"+ str(id) +"'"
    result_product = connect_mysql_get_data(query)
    for data in result_product:
        query_id = "Select NameCategory from category where IdCategory = '"+ str(data[4]) +"'"
        IdCategory = connect_mysql_get_data(query_id)
        result = {
            'IdProduct': data[0],
            'NameProduct': data[1],
            'Price': data[2],
            'Description': data[3],
            'IdCategory': data[4],
            'NameCategory': IdCategory[0][0],
        }

    query_category = "Select * from category"
    result_list_category = connect_mysql_get_data(query_category)
    result_category = []
    for data in result_list_category:
        result_category.append({
            'IdCategory': data[0],
            'NameCategory': data[1],
        })
    context = {'Product': result, 'listCategory': result_category}
    return render(request, 'pages/updateProduct.html', context)

def updateStaff(request, id):

    if request.method == "POST":
        LastName = request.POST['lastname']
        FirstName = request.POST['firstname']
        Email = request.POST['email']
        numberphone = request.POST['numberphone']
        password = request.POST['password']

        query = "update `user` set `FisrtName` = '"+ FirstName +"', `LastName` = '"+ LastName +"', `Email` = '"+ Email +"', `Pass_word` = '"+ password +"', `Phone_number` = '"+ numberphone +"' where `ID`='"+ str(id) +"'"

        connect_mysql(query)

        return redirect("Admin:staffaccounts")

    query = "Select * from user where ID='"+ str(id) +"'"
    data = connect_mysql_get_data(query)
    print(data)
    result = {
        'ID': data[0][0],
        'FisrtName': data[0][1],    
        'Email': data[0][2],
        'PassWord': data[0][3],
        'PhoneNumber': data[0][4],
        'LastName': data[0][6],
    }

    context = {'staff': result}
    return render(request, 'pages/updateStaff.html', context)


def listStaffSales(request):
    return render(request, 'pages/listStaffSales.html')