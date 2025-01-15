import mysql.connector

def owner():
    cnx = mysql.connector.connect(
                user="Practice",
                password="Root",
                host="localhost",
                database="inventory")
    cur=cnx.cursor()

    query="CREATE TABLE IF NOT EXISTS Owner(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL)"

    cur.execute(query)

    cnx.commit()

    cnx.close()
def items():
    cnx = mysql.connector.connect(
                user="Practice",
                password="Root",
                host="localhost",
                database="inventory")
    cur=cnx.cursor()

    query="CREATE TABLE IF NOT EXISTS Items(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,ownerid INT NOT NULL,itemname VARCHAR(255) NOT NULL,Ordered_quantity INT NOT NULL, Available_quantity INT NOT NULL, order_price INT NOT NULL,selling_price INT NOT NULL,date DATETIME NOT NULL,FOREIGN KEY (ownerid) REFERENCES Owner(id))"

    cur.execute(query)

    cnx.commit()

    cnx.close()
def sold():
    cnx = mysql.connector.connect(
                user="Practice",
                password="Root",
                host="localhost",
                database="inventory")
    cur=cnx.cursor()

    query="CREATE TABLE IF NOT EXISTS Sold(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,itemid INT NOT NULL,sold_quantity INT NOT NULL, selling_price INT NOT NULL, discount_amount INT NOT NULL, date DATETIME NOT NULL,FOREIGN KEY (itemid) REFERENCES Items(id))"

    cur.execute(query)

    cnx.commit()

    cnx.close()
def Codes():
    cnx = mysql.connector.connect(
                user="Practice",
                password="Root",
                host="localhost",
                database="inventory")
    cur=cnx.cursor()

    query="CREATE TABLE IF NOT EXISTS Codes(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,code VARCHAR(255)NOT NULL,amount INT NOT NULL,ownerid INT NOT NULL, date DATETIME NOT NULL,FOREIGN KEY (ownerid) REFERENCES Owner(id))"

    cur.execute(query)

    cnx.commit()

    cnx.close()

def database():
    cnx = mysql.connector.connect(
                user="Practice",
                password="Root",
                host="localhost")
    cur=cnx.cursor()

    query="CREATE DATABASE IF NOT EXISTS inventory"

    cur.execute(query)

    cnx.commit()

    cnx.close()

i=0


for i in range(5):

    if i==0:
        database()
        print("Database available!\n")
        i+=1
    if i==1:
        owner()
        print("Owner table available!\n")
        i+=1
    if i==2:
        items()
        print("Items table available!\n")
        i+=1
    if i==3:
        sold()
        print("Sold table available!\n")
        i+=1
    if i==4:
        Codes()
        print("Codes table available!\n")
        break
    

# Display total profit
            