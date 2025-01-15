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

choice=input("""Press:
(1)To create Owners table.
(2)To create Items table.
(3)To create Sold items table.\n""")

if choice=="1":
    owner()
elif choice=="2":
    items()
elif choice=="3":
    sold()
else:
    print("Invalid option chosen.")