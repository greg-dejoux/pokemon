from eau import Eau
from normal import Normal
from feu import Feu
from terre import Terre
import time


class Pokemon:

    def __init__(self):
        nom = "Pokemon"
        niveau = 1
        hp = 100
        attaque = 0
        defense = 0
        type1 = "Type1"
        type2 = "Type2"
        damage = attaque
        self.damage = damage
        self.nom = nom
        self.niveau = niveau
        self.hp = hp
        self.defense = defense
        self.attaque = attaque
        self.type1 = type1
        self.type2 = type2

    def choix_pokemon1(self):
        continuer = False
        while not continuer:
            self.type1 = input("Veuillez choisir le type de votre Pokemon entre eau/feu/terre/normal\n(en minuscule "
                               "svp) =")
            if self.type1 == 'eau':
                self.type1 = Eau.__init__(self)
                print("Vous allez jouer avec ce Pokemon de type Eau:")
                self.show_caracteristiques()
                continuer = True
                return self.type1
            elif self.type1 == 'normal':
                self.type1 = Normal.__init__(self)
                print("Vous allez jouer avec ce Pokemon de type Normal:")
                self.show_caracteristiques()
                continuer = True
                return self.type1
            elif self.type1 == 'feu':
                self.type1 = Feu.__init__(self)
                print("Vous allez jouer avec ce Pokemon de type Feu:")
                self.show_caracteristiques()
                continuer = True
                return self.type1
            elif self.type1 == 'terre':
                Terre.__init__(self)
                print("Vous allez jouer avec ce Pokemon de type Terre:")
                self.show_caracteristiques()
                continuer = True
                return self.type1
            else:
                pass

    def choix_pokemon2(self):
        continuer = False
        while not continuer:
            self.type2 = input("Veuillez choisir le type du Pokemon de votre adversaire entre eau/feu/terre/normal\n("
                               "en minuscule svp) =")
            if self.type2 == 'eau':
                self.type2 = Eau.__init__(self)
                print("Votre adversaire va jouer avec ce Pokemon de type Eau:")
                self.show_caracteristiques()
                continuer = True
                return self.type2
            elif self.type2 == 'normal':
                Normal.__init__(self)
                print("Votre adversaire va jouer avec ce Pokemon de type Normal:")
                self.show_caracteristiques()
                continuer = True
                return self.type2
            elif self.type2 == 'feu':
                Feu.__init__(self)
                print("Votre adversaire va jouer avec ce Pokemon de type Feu:")
                self.show_caracteristiques()
                continuer = True
                return self.type2
            elif self.type2 == 'terre':
                Terre.__init__(self)
                print("Votre adversaire va jouer avec ce Pokemon de type Terre:")
                self.show_caracteristiques()
                continuer = True
                return self.type2
            else:
                pass


    def show_caracteristiques(self):
        print("Nom =", self.nom, "\nNiveau =", self.niveau, "\nVie =", self.hp, "\nDéfense =", self.defense,
              "\nAttaque =", self.attaque, "\n"
                                           "----------------------------------------------------------------------------------")

# joueur1 = Pokemon()
# joueur2 = Pokemon()
# joueur1.choix_pokemon()
# joueur2.choix_pokemon()
# joueur1.show_caracteristiques()
# joueur2.show_caracteristiques()
