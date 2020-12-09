from colorama import init
init()
from colorama import Fore, Back, Style
import random

def regles(tour):
    print("Essayez de deviner le mot en 6 lettres")
    print("Si une lettre apparaît en ROUGE, c'est qu'elle est bien placée")
    print("Si une lettre apparaît en JAUNE, c'est qu'elle n'est pas bien placée")
    print("Si une lettre apparaît en BLEU, c'est qu'elle n'est pas dans le mot")
    print("Vous avez 8 chances pour trouver le bon mot")
    print("Le mot peut être au pluriel")
    print("Tour n°",tour)

tour = 1
regles(tour)
motsPossibles = ["wapiti","gloire","donjon","survie","joyeux","kayaks","humain","ocelot","oiseau"]
motAleatoire = random.choice(motsPossibles)
motJoueur = input("Ecrivez un mot en 6 lettres : ")

def verification(motJoueur):
    if (len(motJoueur) < 6):
        input("Ecrivez un mot en 6 lettres : ")
    if (len(motJoueur) < 6):
        input("Ecrivez un mot en 6 lettres : ")
    while (tour < 9):
        for i in range(0,6):
            if motJoueur[i] == motAleatoire[i]:
                print(Back.RED + motJoueur[i], end=" ")
            if motJoueur[i] != motAleatoire[i]:
                print(Back.BLUE + motJoueur[i], end=" ")
verification(motJoueur)


def victoire(motJoueur, motAleatoire, victoire, tour):
    if (motJoueur == motAleatoire):
        victoire = True
    else:
        tour = tour + 1
        print("Tour n°",tour)
        input("Ecrivez un autre mot en 6 lettres : ")
victoire(motJoueur, motAleatoire, victoire, tour)

input()