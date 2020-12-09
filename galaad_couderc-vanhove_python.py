from colorama import init
init()
from colorama import Fore, Back, Style
import random

def regles():
    print("Essayez de deviner le mot en 6 lettres")
    print("Si une lettre apparaît en ROUGE, c'est qu'elle est bien placée")
    print("Si une lettre apparaît en JAUNE, c'est qu'elle n'est pas bien placée")
    print("Si une lettre apparaît en BLEU, c'est qu'elle n'est pas dans le mot")
    print("Vous avez 8 chances pour trouver le bon mot")
    print("Le mot peut être au pluriel")

motsPossibles = ["wapiti","gloire","donjon","survie","joyeux","kayaks","humain","ocelot","oiseau"]
motAleatoire = random.choice(motsPossibles)

motJoueur = input("Ecrivez un mot en 6 lettres")
def verification(motAleatoire):    
    if (len(motJoueur) < 6):
        input("Ecrivez un mot en 6 lettres")
    if (len(motJoueur) < 6):
        input("Ecrivez un mot en 6 lettres")
    else:
        

input()