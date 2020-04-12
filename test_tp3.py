#Laurent Castonguay, Jacob Jacques, Thomas Lallier

import pandas
import mysql.connector
import csv

#with open("stats.csv", "w", newline="") as f:  # code pour créer un csv tiré de : https://www.youtube.com/watch?v=s1XiCh-mGCA
   # writer = csv.writer(f)
   # writer.writerow(["Company_Name;Nb_Orders;Total_Sales;Average_Sales;Total_Freight"])

mydb = mysql.connector.connect(host="gis-ins01.fadm.usherbrooke.ca", user="demo", passwd="Demo5678.", port="3301", database="db-northwind")
mycursor = mydb.cursor()

mycursor.execute("SELECT CustomerID, CompanyName FROM `db-northwind`.Customers")
customers = mycursor.fetchall()

customerid = []
companyname = []
for row in customers:
    customerid.append(row[0])
    companyname.append(row[1])
#print(customerid)
#print(companyname)


mycursor.execute("SELECT OrderID, Freight FROM `db-northwind`.Orders WHERE CustomerID = customerid;")
orders = mycursor.fetchall()

orderid = []
freight = []
#for row in orders:
    #orderid.append(row[0])
    #freight.append(row[1])
#print(orderid)
#print(str(freight))


mycursor.execute("SELECT Discount FROM `db-northwind`.`Order Details`")
details = mycursor.fetchall()

unitprice = []
quantity = []
discount = []

for row in details:
    #unitprice.append(row[0])
    #quantity.append(row[1])
    #discount.append(row[2])
    print(row[0])
#print(unitprice)
#print(quantity)
#print(discount)

