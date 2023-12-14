#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:41:58 2023

@author: awidmer
"""


class utilisateur:

    def __init__(self, userdata):
        self.user_id = userdata[0]
        self.nom = userdata[1]
        self.age = userdata[2]
        self.activite = userdata[3]
        self.amis = userdata[4]

    def affichage(self):
        print(f'identifiant: {self.user_id}')
        print(f'nom: {self.nom}')
        print(f'age: {self.age}')
        print(f'activite: {self.activite}')
        print(f'amis: {self.amis}')
        print()

    def ajouteramis(self, idamis):
        self.amis.append(idamis)


# %%
def userdata(line):
    data = line.strip().split(',')
    user_id = data[0]
    full_name = data[1]
    age = int(data[2])
    is_active = data[3] == "True"
    related_users = data[4:]

    return [user_id, full_name, age, is_active, related_users]


import networkx as nx
import matplotlib.pyplot as plt

with open('users.txt', 'r', encoding='utf-8') as fichier:
    G = nx.Graph()
    liste_users = fichier.readlines()  # liste ou chaque element est une ligne en string

    liste_objets = []

    deja_cree = []

    for i in liste_users:
        user = utilisateur(userdata(i))
        liste_objets.append(user)

        if user.user_id not in deja_cree:
            G.add_node(user.user_id)  # créé une noeud pour chaque utilisateur
            deja_cree.append(user.user_id)

            for ami in user.amis:
                G.add_edge(user.user_id, ami)  # créé les arretes qui relient le amis entre eux

    for objet in liste_objets:
        objet.affichage()

    print(userdata(liste_users[0]))  # affiche la liste de liste de l'utilisateur1
    print()

# Definir la disposition du graphe
pos = nx.spring_layout(G)

# Dessiner les noeuds et les aretes du graphe
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2, edge_color='blue')

# Ajouter des etiquettes aux noeuds
labels = {}
for node in G.nodes():
    labels[node] = node
nx.draw_networkx_labels(G, pos, labels, font_size=10)

# Afficher le graphe
plt.axis('off')
plt.show()

# %%


import networkx as nx
import matplotlib.pyplot as plt
import csv

# Creer le graphe a partir d'un fichier CSV
G = nx.Graph()
with open('chemins.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # sauter l'en-tete
    for row in reader:
        ville_depart, ville_arrivee, type_t, temps_parcours, cout, distance = row[:6]
        G.add_edge(ville_depart, ville_arrivee, temps_parcours=float(temps_parcours), cout=float(cout),
                   distance=float(distance))

# Definir la disposition du graphe
pos = nx.spring_layout(G)

# Dessiner les noeuds et les aretes du graphe
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2, edge_color='blue')

# Ajouter des etiquettes aux noeuds
labels = {}
for node in G.nodes():
    labels[node] = node
nx.draw_networkx_labels(G, pos, labels, font_size=10)

# Afficher le graphe
plt.axis('off')
plt.show()
