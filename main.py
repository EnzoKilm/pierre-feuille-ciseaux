#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Modules
import os
from modules.variables import *
from modules.fonctions import *

# Début du compteur total
time_total_d = time.time()
    
while jouer != 0 :
    # Titre
    print(str(ti_l1) + str(partie) + str(ti_l2))
    
    # Début du compteur partie
    time_partie_d = time.time()

    # Jeu
    jeu()
        
    # Fin du compteur partie
    time_partie_s = time.time()
    # Calcul temps partie
    temps_partie = time_partie_s - time_partie_d
    
    # Résultat
    from modules.fonctions import sc_o, sc_j
    print(trait + "\n\nScore final :\nOrdinateur : " + str(sc_o) + "\nJoueur : " + str(sc_j))
    print("La partie à durée " + str(round(temps_partie,1)) + " secondes.")
    if sc_o > sc_j :
        print("\nL'ordinateur à gagné.\n" + trait)
    elif sc_j > sc_o :
        print("\nLe joueur à gagné.\n" + trait)
        stats_win += 1
    else :
        print("\nÉgalité.\n" + trait)

    # Rejouer
    rejouer = input("\nSouhaitez-vous rejouer ?\n")
    if rejouer.upper() in oui :
        partie += 1
        print(trait)
    elif rejouer.upper() in non :
        jouer = 0
        # Fin du compteur total
        time_total_s = time.time()
        # Calcul temps total
        temps_total = time_total_s - time_total_d
        print(trait)
        
        # Statistiques
        print(st_l1)
        if partie == 1 :
            partie_txt = " partie"
        else :
            partie_txt = " parties"
        print("\nVous avez joué " + str(partie) + partie_txt + " et vous en avez gagné " + str(stats_win) + ".")
        print("Vous avez joué pendant " + str(round(temps_total,1)) + " secondes.")
        print(trait)
        
        # Classement
        # Enregistrement des statistiques actuelles
        nom_joueur = input("\nVotre nom : ")
        path = "./classement/" + nom_joueur
        # On test si le dossier avec le nom du joueur existe
        path_exist = os.path.exists(path)

        # Si il existe on lit les fichiers
        if path_exist == True :
            # Parties gagnées
            # Lecture
            path_file_win = path + "/games_win.txt"
            file_win = open(path_file_win, "r")
            donnees_win = file_win.read()
            file_win.close()
            # Calcul
            donnees_win_int = int(donnees_win)
            donnees_win_int += stats_win
            # Écriture
            path_file_win = path + "/games_win.txt"
            file_win = open(path_file_win, "w")
            file_win.write(str(donnees_win_int))
            file_win.close()
            
            # Parties jouées
            # Lecture
            path_file_played = path + "/games_played.txt"
            file_played = open(path_file_played, "r")
            donnees_played = file_played.read()
            file_played.close()
            # Calcul
            donnees_played_int = int(donnees_played)
            donnees_played_int += partie
            # Écriture
            path_file_played = path + "/games_played.txt"
            file_played = open(path_file_played, "w")
            file_played.write(str(donnees_played_int))
            file_played.close()
            
            # Temps de jeu
            # Lecture
            path_file_time = path + "/time_playing.txt"
            file_time = open(path_file_time, "r")
            donnees_time = file_time.read()
            file_time.close()
            # Calcul
            donnees_time_int = float(donnees_time)
            donnees_time_int += temps_total
            # Écriture
            path_file_time = path + "/time_playing.txt"
            file_time = open(path_file_time, "w")
            file_time.write(str(round(donnees_time_int,1)))
            file_time.close()
            
        # Sinon on le crée
        else :
            os.mkdir(path)
            # Parties gagnées
            # Écriture
            path_file_win = path + "/games_win.txt"
            file_win = open(path_file_win, "w")
            file_win.write(str(stats_win))
            file_win.close()
            
            # Parties jouées
            # Écriture
            path_file_played = path + "/games_played.txt"
            file_played = open(path_file_played, "w")
            file_played.write(str(partie))
            file_played.close()
            
            # Temps de jeu
            # Écriture
            path_file_time = path + "/time_playing.txt"
            file_time = open(path_file_time, "w")
            file_time.write(str(round(temps_total,1)))
            file_time.close()


    # Affichage du classement
        # Séparation + titre
        print(trait + esp + cl_l1 + cl_l2)

    # Parties jouées
        # Afficher les dossiers
        path = "./classement/"
        fichiers = os.listdir(path)
        liste_dossiers = []
        for i in fichiers :
            liste_dossiers.append(i)

        # Trouver les scores
        # Lecture
        x = 0
        liste_pseudo = []
        liste_score = []
        for i in liste_dossiers :
            x += 1
            # Ouverture / lecture du fichier
            path_file = path + i + "/games_played.txt"
            file = open(path_file, "r")
            donnees_file = file.read()
            liste_pseudo.append(i)
            liste_score.append(donnees_file)
            file.close()

        print(cl_titre_played)

        class Pseudo:

            def __init__(self, pseudo, score):
                self.pseudo = pseudo
                self.score = score

            def __repr__(self):
                return "{} \u27A5 {}".format(self.pseudo, self.score)


        liste_classement = []

        for i in range(0, x):
            pseudo = str(liste_pseudo[i])
            score = int(liste_score[i])
            
            liste_classement += [
                Pseudo(pseudo, score),
            ]

        affichage = sorted(liste_classement, key=lambda pseudo: pseudo.score, reverse=True)

        for i in range(0,len(affichage)):
            if i == 0 :
                cl_liste = cl_liste_l1
                print(cl_liste + str(affichage[i]))
            elif i == 1 :
                cl_liste = cl_liste_l2
                print(cl_liste + str(affichage[i]))
            elif i == 2 :
                cl_liste = cl_liste_l3
                print(cl_liste + str(affichage[i]))
            else :
                pass

    # Parties gagnées
        # Afficher les dossiers
        path = "./classement/"
        fichiers = os.listdir(path)
        liste_dossiers = []
        for i in fichiers :
            liste_dossiers.append(i)

        # Trouver les scores
        # Lecture
        x = 0
        liste_pseudo = []
        liste_score = []
        for i in liste_dossiers :
            x += 1
            # Ouverture / lecture du fichier
            path_file = path + i + "/games_win.txt"
            file = open(path_file, "r")
            donnees_file = file.read()
            liste_pseudo.append(i)
            liste_score.append(donnees_file)
            file.close()

        print(cl_titre_win)

        class Pseudo:

            def __init__(self, pseudo, score):
                self.pseudo = pseudo
                self.score = score

            def __repr__(self):
                return "{} \u27A5 {}".format(self.pseudo, self.score)


        liste_classement = []

        for i in range(0, x):
            pseudo = str(liste_pseudo[i])
            score = int(liste_score[i])
            
            liste_classement += [
                Pseudo(pseudo, score),
            ]

        affichage = sorted(liste_classement, key=lambda pseudo: pseudo.score, reverse=True)

        for i in range(0,len(affichage)):
            if i == 0 :
                cl_liste = cl_liste_l1
                print(cl_liste + str(affichage[i]))
            elif i == 1 :
                cl_liste = cl_liste_l2
                print(cl_liste + str(affichage[i]))
            elif i == 2 :
                cl_liste = cl_liste_l3
                print(cl_liste + str(affichage[i]))
            else :
                pass
         

    # Temps de jeu
        # Afficher les dossiers
        path = "./classement/"
        fichiers = os.listdir(path)
        liste_dossiers = []
        for i in fichiers :
            liste_dossiers.append(i)

        # Trouver les scores
        # Lecture
        x = 0
        liste_pseudo = []
        liste_score = []
        for i in liste_dossiers :
            x += 1
            # Ouverture / lecture du fichier
            path_file = path + i + "/time_playing.txt"
            file = open(path_file, "r")
            donnees_file = file.read()
            liste_pseudo.append(i)
            liste_score.append(donnees_file)
            file.close()

        print(cl_titre_time)

        class Pseudo:

            def __init__(self, pseudo, score):
                self.pseudo = pseudo
                self.score = score

            def __repr__(self):
                return "{} \u27A5 {}".format(self.pseudo, self.score)


        liste_classement = []

        for i in range(0, x):
            pseudo = str(liste_pseudo[i])
            score = float(liste_score[i])
            
            liste_classement += [
                Pseudo(pseudo, score),
            ]

        affichage = sorted(liste_classement, key=lambda pseudo: pseudo.score, reverse=True)

        for i in range(0,len(affichage)):
            if i == 0 :
                cl_liste = cl_liste_l1
                print(cl_liste + str(affichage[i]))
            elif i == 1 :
                cl_liste = cl_liste_l2
                print(cl_liste + str(affichage[i]))
            elif i == 2 :
                cl_liste = cl_liste_l3
                print(cl_liste + str(affichage[i]))
            else :
                pass


        # Séparation
        print(esp + trait)
        
    else :
        ("Réponse incorrecte, veuillez réessayer.")
