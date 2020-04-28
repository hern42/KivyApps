from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from random import randrange

montant_cagnotte = 1000
liste_choix = ['pair', 'impair', 'noir', 'rouge', 'passe', 'manque', 'nombre']
liste_nombre = [i for i in range(1, 37)]


# définition des couleurs
# rouge = [1,3,5,7,9,1,14,16,18,19,21,23,25,27,30,32,34,36]
# noir correspond au complémentaire à 36
# manque correspond aux nombres entre 1 à 18, passe de 19 à 36
# le 0 est la banque.

def check_couleur(bille):
    rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if bille in rouge:
        couleur = 'rouge'
    else:
        couleur = 'noir'
    return couleur


def check_manque_passe(bille):
    if bille <= 18:
        passe_manque = 'manque'
    else:
        passe_manque = 'passe'
    return passe_manque


def check_pair_impair(bille):
    if bille % 2 == 1:
        parite = 'impair'
    else:
        parite = 'pair'
    return parite


# on tire un nombre au hasard entre 0 et 36
def roulette():
    bille = randrange(0, 36)
    return bille


def calcul_gain(mise, choix):
    mise = int(mise)
    if choix.isdigit():
        gain = mise * 35
    else:
        gain = mise
    return gain


class RouletteGame(GridLayout):
    def game(self, pari, mise):
        global montant_cagnotte
        if montant_cagnotte <= 0:
            self.display1.text = 'Perdu... Vous êtes ruiné.'
        else:
            # on récupère la bille courante...
            bille = roulette()
            couleur = check_couleur(bille)
            passe_manque = check_manque_passe(bille)
            parite = check_pair_impair(bille)
            resultat_roulette = [str(bille), couleur, parite, passe_manque]
            resultat_string = str(bille) + ' - ' + couleur.capitalize() + ' - ' + parite.capitalize() + ' - ' + \
                              passe_manque.capitalize()

            # on récupère ce que veut parier le joueur et sa mise
            montant_mise = int(mise)
            pari_joueur = pari.lower()

            # on teste si on a gagné
            if bille == 0:
                self.display1.text = '0 ! La banque gagne...'
                gain = -1 * montant_mise
            elif pari_joueur in resultat_roulette:
                gain = calcul_gain(montant_mise, pari_joueur)
                self.display1.text = resultat_string + '\nGagné ! ' + str(gain) + ' boulles.'
            else:
                self.display1.text = resultat_string + '\nPerdu ! '
                gain = -1 * montant_mise

            # mise à jour de la cagnotte
            montant_cagnotte += gain
            self.display0.text = str(montant_cagnotte) + ' boulles.'

            # remise à zéro de la case mise...
            self.display2.text = ''


class RouletteApp(App):
    def build(self):
        return RouletteGame()


if __name__ == '__main__':
    RouletteApp().run()