#Laurent Castonguay, Jacob Jacques, Thomas Lallier

import pandas
import mysql.connector
import csv

#with open("stats.csv", "w", newline="") as f:  # code pour créer un csv tiré de : https://www.youtube.com/watch?v=s1XiCh-mGCA
   # writer = csv.writer(f)
   # writer.writerow(["Company_Name;Nb_Orders;Total_Sales;Average_Sales;Total_Freight"])

mydb = mysql.connector.connect(host="gis-ins01.fadm.usherbrooke.ca", user="demo", passwd="Demo5678.", port="3301", database="db-northwind")
mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM `db-northwind`.Customers LEFT JOIN `db-northwind`.Orders ON Orders.CustomerID=Customers.Customer.ID LEFT JOIN `db-northwind`.`Order Details` ON `Orders Details`.OrderID=Orders.OrderID;")
#test = mycursor.fetchall()
#print(test)


mycursor.execute("SELECT CustomerID, CompanyName FROM `db-northwind`.Customers;")
customers = mycursor.fetchall()

completeList = []
for row_customer in customers:
	mycursor.execute("SELECT OrderID, Freight FROM `db-northwind`.Orders WHERE CustomerID = %(customerid)s;",{'customerid': row_customer[0]})
	orders = mycursor.fetchall()
	
	for row_order in orders:
		mycursor.execute("SELECT UnitPrice, Quantity, Discount FROM `db-northwind`.`Order Details` WHERE OrderID = %(orderid)s;",{'orderid': row_order[0]})
		details = mycursor.fetchall()
		
		for row_detail in details:
			completeList.append([row_customer[0],row_customer[1],row_order[0],row_order[1],row_detail[0],row_detail[1],row_detail[2]])
	
print(completeList,sep="\n")

