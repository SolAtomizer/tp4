# TP2 partie_1: Laurent Castonguay, Jacob Jacques, Thomas Lallier TP2 partie_1
import csv
import numpy as np  # nécessaire pour le calcul de corrélation linéaire

items = open("Items.csv", "r")
horaires = open("Horaires.csv", "r")
revenu_jours = open("Revenus.csv", "r")

ventes = csv.reader(items, delimiter=",")
depenses = csv.reader(horaires, delimiter=",")
revenu = csv.reader(revenu_jours, delimiter=",")


def stats_ventes():
    items.seek(0)  # Garanti le retour à la première ligne de la liste lorsque la fonction est appelée
    next(ventes)  # Permet de passer à la ligne suivante du fichier csv, ignorant les entêtes
    total_ventes = 0
    margebb = 0

    for ligne in ventes:
        total_ventes += float(ligne[1]) * float(ligne[3])  # multiplication du nombre d'unités * le prix
        margebb += float(ligne[1]) * (float(ligne[3]) - float(ligne[2]))  # multiplication du nombre d'unités * (prix - coût)
    return total_ventes, margebb


# Cette ligne ci-dessous défini les variables de la fonction et les associe à leurs valeurs calculées par celle-ci
total_ventes, margebb = stats_ventes()


def stats_salaires():
    horaires.seek(0)
    next(depenses)  # Garanti le retour à la première ligne de la liste lorsque la fonction est appelée
    ligne1 = next(depenses)  # ligne1 établi les valeurs de la ligne 1 utilisées pour définir salaire_min et salaire_max
    total_salaires = 0
    salaire_min = float(ligne1[1]) * float(ligne1[2])  # établi la valeur de base (heures * salaires à la ligne 1)
    salaire_max = float(ligne1[1]) * float(ligne1[2])  # idem
    employe_min = ""
    employe_max = ""

    for ligne in depenses:
        total_salaires += float(ligne[1]) * float(ligne[2])
        if float(ligne[1]) * float(ligne[2]) <= salaire_min:
            salaire_min = float(ligne[1]) * float(ligne[2])
            employe_min = ligne[0]  # associe le nom de l'employe à la ligne[0] avec le salaire minimal

        if float(ligne[1]) * float(ligne[2]) >= salaire_max:
            salaire_max = float(ligne[1]) * float(ligne[2])
            employe_max = ligne[0]  # associe le nom de l'employe à la ligne[0] avec le salaire maximal

    return total_salaires, salaire_min, salaire_max, employe_min, employe_max


# Cette ligne ci-dessous défini les variables de la fonction et les associe à leurs valeurs calculées par celle-ci
total_salaires, salaire_min, salaire_max, employe_min, employe_max = stats_salaires()


def stats_visites():
    revenu_jours.seek(0)
    next(revenu)
    visites_totales = 0
    visites_moy = 0
    rb_total = 0
    rb_moy = 0
    col_1 = []  # pour la corrélation, une liste vide est créée et les valeurs de la colonne y sont ajouté par le "for" ci-dessous
    col_2 = []  # idem
    correlation = 0
    force = ""

    for ligne in revenu:
        visites_totales += float(ligne[2])
        visites_moy = visites_totales / float(ligne[0])  # fonctionne grâce à la colonne 1 de revenus.csv qui sert de compteur, sinon un compteur aurait été ajouté pour la division
        rb_total += float(ligne[1])
        rb_moy = rb_total / float(ligne[0])  # idem
        col_1.append(float(ligne[1]))  # dans la liste vide col_1 s'ajoutent les valeurs du revenu brute
        col_2.append(float(ligne[2]))  # dans la liste vide col_2 s'ajoutent les valeurs du nombre de visiteurs

    correlation = np.corrcoef(col_1, col_2)[0, 1]  # grâce a PyCharm, la corrélation des 2 colonnes (en liste) se calcule facilement

    if correlation <= 0.39:  # classes "faible", "modérée" et "forte" provenant de : http://www.statstutor.ac.uk/resources/uploaded/pearsons.pdf, page 4.
        force = "La corrélation entre les revenus et le nombre de visiteurs est considérée faible"
    elif correlation >= 0.4:
        force = "la corrélation entre les revenus et le nombre de visiteurs est considérée modérée"
    if correlation >= 0.6:
        force = "la corrélation entre les revenus et le nombre de visiteurs est considérée forte"

    return visites_totales, visites_moy, rb_total, rb_moy, correlation, force


# Cette ligne ci-dessous défini les variables de la fonction et les associe à leurs valeurs calculées par celle-ci
visites_totales, visites_moy, rb_total, rb_moy, correlation, force = stats_visites()


def imprimer_statistiques_mensuelle(charges_externes):
    margebn = margebb - (total_salaires + charges_externes)

    print("Voici le rapport de statistiques pour: \n" +
          "-Items.csv\n" +
          "-Horaires.csv\n" +
          "-Revenus.csv\n" +
          "++++Revenu ++++\n" +
          "Les ventes totales sont de: " + str(total_ventes) + "\n" +
          "La marge bénéficiaire brute est de: " + str(margebb) + "\n" +
          "----Dépense ----\n" +
          "Le total des salaires est de: " + str(total_salaires) + "\n" +
          "L’employé avec le moindre salaire: " + str(employe_min) + ", " + str(salaire_min) + "\n" +
          "L’employé avec le plus grand salaire: " + str(employe_max) + ", " + str(salaire_max) + "\n" +
          "Les charges externes sont de: " + str(charges_externes) + "\n" +
          "==== Total ====\n" +
          "La marge bénéficiaire nette est de: " + str(margebn) + "\n" +
          "////Statistiques de visites \\\\\\\\" + "\n" +
          "Visites totales: " + str(visites_totales) + "\n" +
          "visites moyennes par jour: " + str(visites_moy) + "\n" +
          "Revenu brute total: " + str(rb_total) + "\n" +
          "Revenu brute moyen par jour: " + str(rb_moy) + "\n" +
          "Facteur de corrélation Revenu vs. Visite: " + str(correlation) + "\n" +
          "Explication: " + str(force))


imprimer_statistiques_mensuelle(1567)
