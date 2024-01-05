# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:27:16 2024

@author: teren
"""
fichier = "users_linked.json"
import fileManager as fm
 
dico=fm.initialiser_dico_utilisateurs_json(fichier)


def supprimer_ami2sens(id_user, id_ami):
    dico[id_user].supprimer_ami(id_ami)
    dico[id_ami].supprimer_ami(id_user)

def ajouter_ami2sens(id_user, id_ami , annees_amitie):
    dico[id_user].ajouter_amis(id_ami , annees_amitie)
    dico[id_ami].ajouter_amis(id_user, annees_amitie)

dico['user1'].affichage()
dico['user9'].affichage()

supprimer_ami2sens('user1', 'user9')


dico['user1'].affichage()
dico['user9'].affichage()
