# Modules externes
import random
import time
import os
# Modules locaux
from modules.variables import *

# Fonctions
def tour_ordinateur():
    global co_j, co_n
    # Nombre aléatoire entre 1 et 3
    co = random.randint(1, 3)
    if co == 1 :
        co_j = "Pierre"
        co_n = 1
    elif co == 2 :
        co_j = "Feuille"
        co_n = 2
    else :
        co_j = "Ciseaux"
        co_n = 3

def tour_joueur():
    global ch_ok, cj_j, cj_n
    # On demande au joueur ce qu'il choisit
    ch_ok = 0
    while ch_ok != 1 :
        cj = input(trait + "\n\nPierre, feuille, ciseaux ? ")
        if cj.upper() in pierre :
            ch_ok = 1
            cj_j = "Pierre"
            cj_n = 1
        elif cj.upper() in feuille :
            ch_ok = 1
            cj_j = "Feuille"
            cj_n = 2
        elif cj.upper() in ciseaux :
            ch_ok = 1
            cj_j = "Ciseaux"
            cj_n = 3
        else :
            print("\nVotre choix est incorrect, veuillez réessayer.")

def comparaison():
    global sc_o, sc_j
    # Égalité
    if co_n == cj_n :
        print(esp + co_j + " contre " + cj_j + " : égalité")
    # Ordinateur gagne
    elif co_n == 2 and cj_n == 1 :
        print(esp + co_j + " contre " + cj_j + " : l'ordinateur gagne")
        sc_o += 1
    elif co_n == 3 and cj_n == 2 :
        print(esp + co_j + " contre " + cj_j + " : l'ordinateur gagne")
        sc_o += 1
    elif co_n == 1 and cj_n == 3 :
        print(esp + co_j + " contre " + cj_j + " : l'ordinateur gagne")
        sc_o += 1
    # Joueur gagne
    elif co_n == 3 and cj_n == 1 :
        print(esp + co_j + " contre " + cj_j + " : le joueur gagne")
        sc_j += 1
    elif co_n == 1 and cj_n == 2 :
        print(esp + co_j + " contre " + cj_j + " : le joueur gagne")
        sc_j += 1
    elif co_n == 2 and cj_n == 3 :
        print(esp + co_j + " contre " + cj_j + " : le joueur gagne")
        sc_j += 1

def jeu():
    global sc_o, sc_j
    sc_o = 0
    sc_j = 0
    # Nombre de parties
    nb_p = int(input("\nNombre de tours : "))
    while nb_p > 0 :
        # L'ordinateur joue
        tour_ordinateur()

        # Le joueur joue
        tour_joueur()
        
        # Comparaison des résultats
        comparaison()

        # Tour suivant
        nb_p -= 1
        if nb_p > 0 :
            print("\nTour suivant")
        else :
            pass
