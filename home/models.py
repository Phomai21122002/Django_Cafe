from django.db import models
import mysql.connector

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
