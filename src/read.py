#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:40:25 2023

@author: cfrindel
"""

# Définir une fonction pour analyser la ligne contenant les données de l'utilisateur
def parse_user_data(line):
    data = line.strip().split(',')
    user_id = data[0]
    full_name = data[1]
    age = int(data[2])
    is_active = data[3] == "True"
    related_users = data[4:]

    return [user_id, full_name, age, is_active, related_users]

# Initialiser une liste pour stocker les données de l'utilisateur
user_object_list = []

# Ouvrir le fichier en lecture
with open("users.txt", "r") as file:
    for line in file:
        user_data = parse_user_data(line)
        user = U.Utilisateur(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        user_object_list.append(user)

# Imprimer les données des utilisateurs
print(user_object_list)
for o in user_object_list:
	o.affichage()
    
print(user_object_list[0].trouver_amis_communs(user_object_list[2]))

# Chercher un utilisateur
