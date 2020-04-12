#TP-2, partie #2 Laurent Castonguay, Thomas Lallier et  Jacob Jacques
def image_ascii(lettre1, lettre2, lettre3, hauteur):                #Définition de la fonction avec ses variables

    separateur = '+'               #Sélection du caractère pour remplir les espaces entre les section générées automatiqument par le code suivant

    for i in range(hauteur):
        i = hauteur - 1 - i             #On inverse le compteur pour pouvoir commencer avec le compteur à la hauteur au lieu de 0
        if i == 0:
            ligneX = lettre1.rjust(hauteur, separateur)
            print(ligneX.ljust((hauteur*2)-1, separateur))          #On fait la condition pour gérer la ligne lorsque seulement le caractère X doit être inscrit

        elif i % 2 == 1 :
            if i == 1:
                ligneZ = (hauteur - (i + 1)) * '+' + lettre1 + lettre3 + lettre1 + (hauteur - (i + 1)) * '+'        #On fait la condition pour gérer la première ligne ayant un Z au milieu
            else:
                ligneZ = (hauteur-(i + 1))*'+' + lettre1+lettre2 + (i-2)*'+' + lettre3 + (i-2)*'+' + lettre2+lettre1 + (hauteur-(i + 1))*'+'    #On gère toutes les autres lignes ayant la lettre Z au milieu
            print(ligneZ)

        else:
            ligneY = (hauteur-(i+1))*'+' + lettre1+lettre3 + (i-2)*'+' + lettre2 + (i-2)*'+' + lettre3+lettre1 + (hauteur-(i+1))*'+'    #On fait la dernière condition pour générer les lignes ayant un Y au milieu
            print(ligneY)

image_ascii('X','Y','Z',9)           #On peut faire la fonction avec n'importe quelle lettre et n'importe quelle hauteur
