from django.db import models
import mysql.connector

class user(models.Model):
    Fisrt_Name = models.TextField()
    Email = models.TextField()
    Pass_Word = models.TextField()
    Phone_Number = models.TextField()
    Classify = models.TextField()
    Last_Name = models.TextField()
    Date = models.DateField()

class orderdetail(models.Model):
    Price = models.IntegerField()
    Number = models.IntegerField()
    Price_Total = models.IntegerField()
    Status = models.IntegerField()

class category(models.Model):
    Name_Category = models.CharField(max_length=50)
    Url_Image = models.TextField()

class product(models.Model):
    Category = models.ForeignKey(category, on_delete=models.CASCADE)
    Name_Product = models.CharField(max_length=50)
    Price = models.IntegerField()
    Description = models.CharField(max_length=50)
    Url_Image = models.TextField()

class order(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE)
    Product = models.ManyToManyField(product)
    Price_Total = models.IntegerField()
    Name_Product = models.CharField(max_length=50)
    Number = models.IntegerField()
    Order_Detail = models.ForeignKey(orderdetail, on_delete=models.CASCADE)

def Login(Email, PassWord):
    listUser = user.objects.all()
    for data in listUser:
        if (data.Email == Email) and (data.Pass_Word == PassWord):
            result = user.objects.get(Email = Email, Pass_Word = PassWord)
            break
        else:
            result = 0
    return result

def Register(FirstName, Email, PassWord, NumberPhone, Classify, LastName, Date):
    User = user(Fisrt_Name = FirstName, Email = Email, Pass_Word = PassWord, Phone_Number = NumberPhone, Classify = Classify, Last_Name = LastName, Date = Date)
    User.save()

def addcategory(Name_Category):
    Category = category(Name_Category = Name_Category)
    Category.save()

def listcategory():
    listCategory = category.objects.all()
    return listCategory

def addproduct(Name_Product, Price, Description, Url_Image, Category_id):
    Product = product(Name_Product = Name_Product, Price = Price, Description = Description, Url_Image = Url_Image, Category_id = Category_id)
    Product.save()

def listproduct():
    listProduct = product.objects.all()
    return listProduct

def get_product_by_category_id(id):
    listCategory = product.objects.filter(Category_id = id)
    return listCategory

def get_different_product(id):
    listCategory = product.objects.exclude(Category_id = id)
    return listCategory

def get_product_by_id(id):
    Product = product.objects.get(id = id)
    return Product

def get_staff_by_id(id):
    staff = user.objects.get(id = id)
    return staff

def liststaff():
    listStaff = user.objects.filter(Classify = 1)
    return listStaff

def updateproduct(id, Name_Product, Price, Description, Category_id):
    product.objects.filter(id = id).update(Name_Product = Name_Product, Price = Price, Description = Description, Category_id = Category_id)

def updatestaff(id, First_Name, Email, Pass_Word, Number_Phone, Last_Name, Date):
    user.objects.filter(id = id).update(Fisrt_Name = First_Name, Email = Email, Pass_Word = Pass_Word, Phone_Number = Number_Phone, Last_Name = Last_Name, Date = Date)

def connect_mysql(query):
    mydb = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = '',
        database = 'quanlycafe',
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()


def connect_mysql_get_data(query):
    mydb = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = '',
        database = 'quanlycafe',
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def listCategory():
    query = "Select * from category"
    result_list_category = connect_mysql_get_data(query)
    result = []
    for data in result_list_category:
        result.append({
            'IdCategory': data[0],
            'NameCategory': data[1],
        })
    return result



# Create your models here.
