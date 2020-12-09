from colorama import init
init()
from colorama import Fore, Back, Style
import random

def regles(tour):
    print("  __________________________________________________________________________")
    print(" | - Essayez de deviner le mot en 6 lettres                                 |")
    print(" | - Si une lettre apparaît en ROUGE, c'est qu'elle est bien placée         |")
    print(" | - Si une lettre apparaît en JAUNE, c'est qu'elle n'est pas bien placée   |")
    print(" | - Si une lettre apparaît en BLEU, c'est qu'elle n'est pas dans le mot    |")
    print(" | - Vous avez 8 chances pour trouver le bon mot                            |")
    print(" | - Attention, le mot peut être au pluriel                                 |")
    print(" |__________________________________________________________________________|")
    print("Tour n°",tour)

tour = 1
regles(tour)
motsPossibles = ["wapiti","gloire","donjon","survie","joyeux","kayaks","humain","ocelot","oiseau","castor","cinema","citron"]
motAleatoire = random.choice(motsPossibles)
motJoueur = ("")
victoire = False

def victoire(motJoueur, motAleatoire, victoire, tour):
    if (motJoueur == motAleatoire):
        victoire = True
        input("Félicitation, vous avez trouvé le bon mot !")
    else:
        tour = tour + 1
        print("Tour n°",tour)
    verification(motJoueur, motAleatoire,tour, victoire)
    return motJoueur, motAleatoire

def verification(motJoueur, motAleatoire,tour, victoire):
    while (tour < 8 and victoire != False):
        motJoueur = input("Ecrivez un mot en 6 lettres : ")
        if (len(motJoueur) < 6):
            motJoueur = input("Ecrivez un mot en 6 lettres : ")
        if (len(motJoueur) > 6):
            motJoueur = input("Ecrivez un mot en 6 lettres : ")
        for i in range(len(motJoueur)):
            if motJoueur[i] == motAleatoire[i]:
                print(Back.RED + motJoueur[i], end=" ")
            if motJoueur[i] != motAleatoire[i]:
                print(Back.BLUE + motJoueur[i], end=" ")
            print(Style.RESET_ALL)
        victoire(motJoueur, motAleatoire, victoire, tour)
    print("Perdu!!!")
    return motJoueur, motAleatoire

verification(motJoueur, motAleatoire,tour, victoire)

input()