#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:04:24 2023

@author: frindel
"""


# Définition de la classe Utilisateur
class Utilisateur:
    def __init__(self, user_id, nom, age, activite, amis):
        self.user_id = user_id
        self.nom = nom
        self.age = age
        self.activite = activite
        self.amis = amis

    def affichage(self):
        print(f'identifiant: {self.user_id}')
        print(f'nom: {self.nom}')
        print(f'age: {self.age}')
        print(f'activité: {self.activite}')
        print(f'amis: {self.amis}')
        print()


# Création d'utilisateurs en utilisant le constructeur
utilisateur1 = Utilisateur('noabng', 'Noa Benoit-Gonnin', 20, False, ['Illona', 'Julia', 'Elsa', 'Louison'])
utilisateur2 = Utilisateur('liobng', 'Lio Benoit-Gonnin', 15, True, ['Rose', 'Eline', 'Alicia'])
utilisateur3 = Utilisateur('maebng', 'Mae Benoit-Gonnin', 18, True, ['Jade', 'Orane', 'Elise', 'Agathe', 'Hugo'])

# Affichage des utilisateurs
utilisateur1.affichage()
utilisateur2.affichage()
utilisateur3.affichage()
