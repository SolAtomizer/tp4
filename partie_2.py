# Laurent Castonguay, Jacob Jacques, Thomas Lallier TP3
# Classe mère
class Robot:
    def __init__(self, type, version):
        self.type = type
        self.version = version
        self.enFonction = False

    def action(self):
        if self.type == "aspirateur":
            # Démarre les capteurs de position
            # Démarre le moteur
            # Autres code ici à mettre pour faire fonctionner l’aspirateur
            print("En action! Le robot aspire les saletés et se retourne face aux obstacles!")
        else:
            # Démarre les capteurs de position
            # Démarre le moteur
            # Autres code ici à mettre pour faire fonctionner la tondeuse
            print("En action! Le robot coupe le gazon et se retourne face aux obstacles!")

    def arret(self):
        # Mettre ici le code pour arrêter le moteur et les capteurs
        print("En arrêt ...")
        self.enFonction = False

    def demarrer(self):
        print("En démarrage ...")
        self.enFonction = True
        # Appel de la fonction qui met le robot en action
        self.action()

    def is_en_fonction(self):
        return self.enFonction


# Classe fille aspirateur
class RobotAspirateur(Robot):

    def __init__(self, version):
        self.version = version
        self.enFonction = False

    def action(self):
        # Démarre les capteurs de position
        # Démarre le moteur
        # Autres code ici à mettre pour faire fonctionner l’aspirateur
        print("En action! Le robot aspire les saletés et se retourne face aux obstacles!")

    def arret(self):
        # Mettre ici le code pour arrêter le moteur et les capteurs
        print("En arrêt ...")
        self.enFonction = False

    def demarrer(self):
        print("En démarrage ...")
        self.enFonction = True
        # Appel de la fonction qui met le robot en action
        self.action()

    def is_en_fonction(self):
        return self.enFonction


# Classe fille tondeuse
class RobotTondeuse(Robot):
    def __init__(self, version):
        self.version = version
        self.enFonction = False

    def action(self):
        # Démarre les capteurs de position
        # Démarre le moteur
        # Autres code ici à mettre pour faire fonctionner l’aspirateur
        print("En action! Le robot coupe le gazon et se retourne face aux obstacles!")

    def arret(self):
        # Mettre ici le code pour arrêter le moteur et les capteurs
        print("En arrêt ...")
        self.enFonction = False

    def demarrer(self):
        print("En démarrage ...")
        self.enFonction = True
        # Appel de la fonction qui met le robot en action
        self.action()

    def is_en_fonction(self):
        return self.enFonction
