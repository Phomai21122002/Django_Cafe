from django.db import models
from datetime import datetime
from django.db.models import Q

class user(models.Model):
    Fisrt_Name = models.TextField()
    Email = models.TextField()
    Pass_Word = models.TextField()
    Phone_Number = models.TextField()
    Classify = models.TextField()
    Last_Name = models.TextField()
    Date = models.DateField()

class orderdetail(models.Model):
    Number = models.IntegerField()
    Price_Total = models.IntegerField()
    Number_Phone = models.CharField(max_length=10, blank=True)
    Address = models.CharField(max_length=255, blank=True)
    DateTime = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField()

class category(models.Model):
    Name_Category = models.CharField(max_length=50)
    Url_Image = models.ImageField(upload_to='home/static/img', null=False, default=None)

class product(models.Model):
    Category = models.ForeignKey(category, on_delete=models.CASCADE)
    Name_Product = models.CharField(max_length=50)
    Price = models.IntegerField()
    Description = models.CharField(max_length=50)
    Url_Image = models.ImageField(upload_to='home/static/img', null=False, default=None)

class order(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE)
    # Product = models.ManyToManyField(product)
    Price = models.IntegerField()
    Price_Total = models.IntegerField()
    Name_Product = models.CharField(max_length=50)
    Number = models.IntegerField()
    Order_Detail = models.ForeignKey(orderdetail, on_delete=models.CASCADE)
    # Status = models.IntegerField()

class orderProduct(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)

def getUserByID(id):
    return user.objects.get(id = id)
    
def updateProfile(id,firstName , lastName , phoneNumber):
   user.objects.filter(id = id).update(Fisrt_Name = firstName, Phone_Number = phoneNumber, Last_Name = lastName)

def resetPass(id):
    user.objects.filter(id = id).update(Pass_Word = '12345678')
    

def updatePass(id,newPass):
    user.objects.filter(id = id).update(Pass_Word = newPass)

def Login(Email, PassWord):
    data = user.objects.filter(Q(Email = Email) & Q(Pass_Word = PassWord))
    return data

    # listUser = user.objects.all()
    # for data in listUser:
    #     if (data.Email == Email) and (data.Pass_Word == PassWord):
    #         result = user.objects.get(Email = Email, Pass_Word = PassWord)
    #         classify = result.Classify
    #         break
    #     elif( (data.Email != Email) and (data.Pass_Word == PassWord)):
    #         result = user.objects.get(Pass_Word = PassWord)
    #         classify = result.Classify
    #         break
    #     elif( (data.Email == Email) and (data.Pass_Word != PassWord)):
    #         result = user.objects.get(Email = Email)
    #         classify = result.Classify
    #         break
    #     else:
    #         result = 0
    #         classify = 0
    
    # return result, classify

def Register(FirstName, Email, PassWord, NumberPhone, Classify, LastName, Date):
    User = user(Fisrt_Name = FirstName, Email = Email, Pass_Word = PassWord, Phone_Number = NumberPhone, Classify = Classify, Last_Name = LastName, Date = Date)
    User.save()

def addcategory(Name_Category, Image):
    Category = category(Name_Category = Name_Category, Url_Image = Image)
    Category.save()

def get_category_by_id(id):
    Category = category.objects.get(id = id)
    return Category

def listcategory():
    listCategory = category.objects.all()
    return listCategory

def deleteCategory(idCategory):
    category.objects.filter(id=idCategory).delete()

def addproduct(Name_Product, Price, Description, Url_Image, Category_id):
    Product = product(Name_Product = Name_Product, Price = Price, Description = Description, Url_Image = Url_Image, Category_id = Category_id)
    Product.save()

def add_order_product(order_id, product_id):
    result = orderProduct(order_id = order_id, product_id = product_id)
    result.save()

def addOrder_get_id(Price, Price_Total, Name_Product, Number, User_id, Order_Detail_id):
    result = order(Price = Price, Price_Total = Price_Total, Name_Product = Name_Product, Number = Number, User_id = User_id, Order_Detail_id = Order_Detail_id)
    result.save()
    Order_id = result.id
    return Order_id

def addOrderDetail_get_id(Number, Price_Total, Status, Number_Phone, Address, Date_Time):
    OrderDetail = orderdetail(Number = Number, Price_Total = Price_Total, Status = Status, Number_Phone = Number_Phone, Address = Address, DateTime = Date_Time)
    OrderDetail.save()
    OrderDetail_id = OrderDetail.id
    return OrderDetail_id

def updateOrder(id, Price, Price_Total, Name_Product, Number, User_id, Order_Detail_id):
    result = order.objects.get(id = id)
    result.Price = Price
    result.Price_Total = Price_Total
    result.Name_Product = Name_Product
    result.Number = Number
    result.User_id = User_id
    result.Order_Detail_id = Order_Detail_id
    result.save()

def updateOrderDetail(id, Number, Price_Total, Status):
    OrderDetail = orderdetail.objects.get(id = id)
    OrderDetail.Number = Number
    OrderDetail.Price_Total = Price_Total
    OrderDetail.Status = Status
    OrderDetail.save()

def update_category(id, Name_Category, Url_Image):
    Category = category.objects.get(id = id)
    Category.Name_Category = Name_Category
    Category.Url_Image = Url_Image
    Category.save()

def listOrderDetail():
    resultOrderDetail = orderdetail.objects.all()
    return resultOrderDetail


def listproduct():
    listProduct = product.objects.all()
    return listProduct

def get_order_by_idOrderDetail(id):
    result = order.objects.filter(Order_Detail_id = id)
    return result

def get_product_by_category_id(id):
    listCategory = product.objects.filter(Category_id = id)
    return listCategory

# lay ra cac ptu khac
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
    listStaff = user.objects.filter(Classify = 2)
    return listStaff

def updateproduct(id, Name_Product, Price, Description, Url_Image, Category_id):
    Product = product.objects.get(id = id)
    Product.Name_Product = Name_Product
    Product.Price = Price
    Product.Description = Description
    Product.Url_Image = Url_Image
    Product.Category_id = Category_id
    Product.save()

def updatestaff(id, First_Name, Email, Pass_Word, Number_Phone, Last_Name, Date):
    User = user.objects.filter(id = id).update(Fisrt_Name = First_Name, Email = Email, Pass_Word = Pass_Word, Phone_Number = Number_Phone, Last_Name = Last_Name, Date = Date)

def resetpass(id):
    User = user.objects.filter(id = id).update(Pass_Word = 123456)

def deletestaff(id):
    User = user.objects.get(id = id)
    User.delete()

def deleteProduct_Order(idProduct):
    ProductOrder = orderProduct.objects.filter(product_id = idProduct)
    for i in ProductOrder:
        i.delete()

def deleteProduct(idProduct):
    Product = product.objects.get(id = idProduct)
    Product.delete()

def deleteCategory(idCategory):
    Products = product.objects.filter(Category_id = idCategory)
    for Product in Products:
        deleteProduct_Order(Product.id)
        deleteProduct(Product.id)
    Category = category.objects.get(id = idCategory)
    Category.delete()
        

def sales_product(Status):
    result_orderDetail = None
    result_order = []
    result_orderDetail = orderdetail.objects.exclude(Status = Status).order_by('-DateTime')
    for data in result_orderDetail:
        result_order.append(order.objects.filter(Order_Detail_id = data.id))
    return result_orderDetail, result_order

def sales_product_by_id(idOrderDetail):
    result_orderDetail = None
    result_order = []
    result_orderDetail = orderdetail.objects.get(id = idOrderDetail)
    result_staff = order.objects.filter(Order_Detail_id = result_orderDetail.id)[:1]
    id_staff = result_staff[0].User_id
    result_user = user.objects.get(id = id_staff)
    result_order.append(order.objects.filter(Order_Detail_id = result_orderDetail.id))
    return result_orderDetail, result_order, result_user

def update_sales(id, id_session):
    result = orderdetail.objects.get(id = id)
    result.Status = 1
    result.DateTime = datetime.now()
    result.save()
    resultOrder = order.objects.get(Order_Detail_id = id)
    resultOrder.User_id = id_session
    resultOrder.save()

def revenue_product(Status):
    result_orderDetail = None
    result_order = []
    result_orderDetail = orderdetail.objects.filter(Status = Status).order_by('-DateTime')        
    for data in result_orderDetail:
        result_order.append(order.objects.filter(Order_Detail_id = data.id))
    return result_orderDetail, result_order

def handle_order(carts, Number_Phone, Address):
    listCart = []
    tatol_product = 0
    tatol_price = 0

    # lay du lieu tu cookies
    for cart in carts:
        product = get_product_by_id(cart['idProduct'])
        listCart.append({
            'idProduct': product.id,
            'Name_Product': product.Name_Product,
            'Price': product.Price,
            'count': int(cart['count']),
            'total': int(cart['count'])*product.Price,
        })
        tatol_product += int(cart['count'])
        tatol_price +=  int(cart['count'])*product.Price
    # da thanh toan thi them vao cai moi va them
    id = addOrderDetail_get_id(tatol_product, tatol_price, 0, Number_Phone, Address, datetime.now())
    for data in listCart:
        order_id = addOrder_get_id(data['Price'], data['total'], data['Name_Product'], data['count'], 1, id)
        add_order_product(order_id, data['idProduct'])


