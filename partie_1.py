# Laurent Castonguay, Jacob Jacques, Thomas Lallier TP3

import pandas
import mysql.connector
import csv

fichier = open("stats.csv", "w", newline="")
writer = csv.writer(fichier, delimiter=";") #delimiter choisi selon l'énoncé qui avait des ";"
writer.writerow({"Company_Name", "Nb_Orders", "Total_Sales", "Average_Sales", "Total_Freight"})  # écrit l'entête

mydb = mysql.connector.connect(host="gis-ins01.fadm.usherbrooke.ca", user="demo", passwd="Demo5678.", port="3301",
                               database="db-northwind")
mycursor = mydb.cursor()

mycursor.execute("SELECT CustomerID, CompanyName FROM `db-northwind`.Customers;")
clients = mycursor.fetchall()

for ligne_customer in clients:
    mycursor.execute("SELECT OrderID, Freight FROM `db-northwind`.Orders WHERE CustomerID = %(customerid)s;", {
        'customerid': ligne_customer[0]}) #fait le lien entre les "OrderID" et les "CustomerID"
    # https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/ pour la syntaxe de requête

    orders = mycursor.fetchall()

    if not orders:  # boucle cruciale au fonctionnement du code, les clients sans commandes causent problème sinon.
        writer.writerow({ligne_customer[1], "0", "0", "0", "0"})
        continue

    df = pandas.DataFrame(orders)
    qte = len(orders)  # quantité de commandes est la len d'"order" par client selon la requête la ligne 19
    total = 0
    freight = df[1].sum()  # fait la somme de "freight" par client selon la requête à la ligne 19

    for ligne_order in orders:
        mycursor.execute(
            "SELECT UnitPrice, Quantity, Discount FROM `db-northwind`.`Order Details` WHERE OrderID = %(orderid)s;",
            {'orderid': ligne_order[0]}) #fait le lien entre les "Order Details" et "OrderID", et donc aux "CustomerID"
        details = mycursor.fetchall()

        for ligne_detail in details:# possible de transformer les variables suivantes en int() pour éviter les décimales
            total += ((ligne_detail[0] - ligne_detail[2]) * ligne_detail[1])  # coût total est (prix-rabais)*quantité

    writer.writerow([ligne_customer[1], str(qte), str(total), str(total / qte), str(freight)])  # écrit le csv complet
fichier.close()  # non nécessaire, bonne pratique
