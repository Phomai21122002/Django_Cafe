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