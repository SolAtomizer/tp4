# Laurent Castonguay, Jacob Jacques, Thomas Lallier
import csv

fichier = open("sales.csv", "r")
resultat = open("vente_annuelle", "w")
csv_reader = csv.reader(fichier, delimiter=";")


def total(annee):
    fichier.seek(0)
    ventes = 0
    for colonne in csv_reader:
        if colonne[9] == str(annee):
            ventes += float(colonne[2]) * float(colonne[1])
    return ventes


resultat.write("Le total de 2003 est: " + str(total(2003)) + "\n")
resultat.write("le total de 2004 est: " + str(total(2004)) + "\n")
resultat.write("Le total de 2005 est: " + str(total(2005)) + "\n")


fichier.close()
resultat.close()
