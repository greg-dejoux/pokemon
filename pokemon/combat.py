from pokemon import *


class Combat(Pokemon):

    def __init__(self):
        Pokemon.__init__(self)
        self.statutpok = 0

    # Fonction statut pokémon (0 = vivant , 1 = mort), vérifie si pokemon mort et donc finit la partie
    def checkifwon1(self):
        if joueur1.hp <= 0:
            joueur1.statutpok = 1
            print("Le", joueur1.nom, "est ko !")
            print("Combat terminé, le ", joueur2.nom, "ennemi l'emporte\nVous avez perdu...")
            quit()

    def checkifwon2(self):
        if joueur2.hp <= 0:
            joueur2.statutpok = 1
            print("Le", joueur2.nom, "ennemi est ko !")
            print("Combat terminé, le ", joueur1.nom, "l'emporte\nVous avez gagné !")
            quit()

    def gettype1(self):
        return self.type1

    def gettype2(self):
        return self.type2

    def hp_trade1(self):
        # fonction du trade entre pokemon joueur 1 et pokemon joueur 2
        joueur2.hp = (joueur2.hp + joueur2.defense) - joueur1.attaque
        return joueur2.hp

    def hp_trade2(self):
        # fonction du trade entre pokemon joueur 1 et pokemon joueur 2
        joueur1.hp = (joueur1.hp + joueur1.defense) - joueur2.attaque
        return joueur1.hp

    def débutj1(self):
        # renvoie le choix du joueur 1
        super().choix_pokemon1()
        return joueur1.type1

    def débutj2(self):
        # renvoie le choix du joueur 1
        super().choix_pokemon2()
        return joueur2.type2

    def suite(self):
        print("Le combat entre", joueur1.nom, "et", joueur2.nom, "va commencer !\n")
        time.sleep(1.5)
        while joueur1.statutpok != 1 or joueur2.statutpok != 1:  # boucle qui tourne jusqu'a ce que l'un des pok soit ko
            # tour du joueur 1
            time.sleep(0.5)
            print("Le", joueur1.nom, "attaque !")
            print("Il inflige", joueur1.attaque, "points de dégats")
            joueur1.hp_trade1()
            print("Grace à sa défense, le", joueur2.nom, "tank", joueur2.defense, "points de dégats !")
            print("Le", joueur2.nom, "ennemi tombe à", joueur2.hp, "points de vies !\n")
            joueur1.checkifwon1()
            joueur2.checkifwon2()
            # tour du joueur 2
            time.sleep(0.5)
            joueur2.hp_trade2()
            print("Le", joueur2.nom, "attaque !")
            print("Il inflige", joueur2.attaque, "points de dégats")
            print("Grace à sa défense, le", joueur1.nom, "tank", joueur1.defense, "points de dégats !")
            print("Le", joueur1.nom, "tombe à", joueur1.hp, "points de vies !\n")
            joueur1.checkifwon1()
            joueur2.checkifwon2()


joueur1 = Combat()
joueur2 = Combat()

joueur1.débutj1()
joueur2.débutj2()

joueur1.suite()
