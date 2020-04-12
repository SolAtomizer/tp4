# Laurent Castonguay, Jacob Jacques, Thomas Lallier

import pandas
import mysql.connector
import csv

fichier = open("stats.csv", "w",newline="")
writer = csv.writer(fichier, delimiter=";")

tableau =[]
mydb = mysql.connector.connect(host="gis-ins01.fadm.usherbrooke.ca", user="demo", passwd="Demo5678.", port="3301",
                               database="db-northwind")
mycursor = mydb.cursor()

mycursor.execute("SELECT CustomerID, CompanyName FROM `db-northwind`.Customers;")
clients = mycursor.fetchall()

for ligne_customer in clients:
    mycursor.execute("SELECT OrderID, Freight FROM `db-northwind`.Orders WHERE CustomerID = %(customerid)s;", {
        'customerid': ligne_customer[0]})
    # https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

    orders = mycursor.fetchall()
    df = pandas.DataFrame(orders)
    freight = df[1].sum()
    qte = len(orders)
    total = 0

    if not orders:
        tableau.append(ligne_customer[1], "", "", "", "")
        #.writerow({ligne_customer[1], "", "", "", ""})
        continue

    for ligne_order in orders:
        mycursor.execute(
            "SELECT UnitPrice, Quantity, Discount FROM `db-northwind`.`Order Details` WHERE OrderID = %(orderid)s;",
            {'orderid': ligne_order[0]})
        details = mycursor.fetchall()

        for ligne_detail in details:
            total += ((ligne_detail[0] - ligne_detail[2]) * ligne_detail[1])

        freight = ligne_order[1]
    tableau.append([ligne_customer[1], qte, total, total / qte, freight])
    print(tableau)
    writer.writerows(tableau)
   # writer.writerow({ligne_customer[1], str(qte), str(total), str(total / qte), str(freight)})
