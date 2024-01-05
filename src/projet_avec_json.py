# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:45:25 2023

@author: Anton
"""

# Importation des bibliothèques nécessaires

import networkx as nx  # Bibliothèque pour la création et l'analyse de graphes
import matplotlib.pyplot as plt  # Bibliothèque pour le traçage de graphiques
import fileManager as fm





# Définition du dictionnaire d'utilisateurs
fichier = "users_linked.json"
dico_utilisateurs = fm.initialiser_dico_utilisateurs_json(fichier)

# modification du dictionnaire avec les méthodes choisies, avant d'afficher le graphe
def nv_dico():
    fm.supprimer_ami2sens('user1', 'user9', dico_utilisateurs)
    fm.ajouter_ami2sens('user1', 'user2', 22, dico_utilisateurs)
    fm.creer_profil("Jackie Chan", 25, True, [{'id_ami': 'user8', 'annees_d_amitie': 10},{'id_ami': 'user7', 'annees_d_amitie': 13}], dico_utilisateurs)
    fm.supprimer_profil('user9', dico_utilisateurs)
    fm.creer_profil("Hervé Biz", 55, True, [{'id_ami': 'user5', 'annees_d_amitie': 30},{'id_ami': 'user2', 'annees_d_amitie': 13}], dico_utilisateurs)
    return dico_utilisateurs

dico_utilisateurs = nv_dico()




def main():
    # Création d'un graphe à l'aide de NetworkX
    G = nx.Graph()
    
    # Modification du dictionnaires avant la création du graphe
    

    # Parcours de chaque utilisateur et de ses amis pour ajouter des arêtes au graphe
    for utilisateur in dico_utilisateurs.values():
        for ami in utilisateur.amis:
            G.add_edge(utilisateur.user_id, ami["id_ami"], annees = ami["annees_d_amitie"])

    pos = nx.spring_layout(G)

    # Dessin des noeuds avec une couleur et une taille spécifiques
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    # Dessin des arêtes avec une largeur et une couleur spécifiques
    edge_labels = {(u, v): d['annees'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edges(G, pos, width=2, edge_color='grey')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')


    # Ajout des étiquettes (noms d'utilisateurs) aux noeuds du graphe
    labels = {}
    for node in G.nodes():
        labels[node] = node
    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    # Désactivation des axes
    plt.axis('off')

    # Affichage du graphe
    plt.show()


# Point d'entrée du programme
if __name__ == "__main__":
    main()




    
#%%
import math


def pop_min(a_explorer):
    
    d_min = math.inf
    sommet_min=""
    for s, d in a_explorer.items():
       
        if d < d_min:
            d_min = d
            sommet_min = s
            
    a_explorer.pop(sommet_min)
    
    return sommet_min, d_min

def dijkstra(depart):
    a_explorer = {depart: 0}
    
    for i in dico_utilisateurs:
        if i != depart:
            a_explorer[i] = math.inf
         
    deja_collectes = {}
    
    while len(a_explorer) != 0:
        courant, distance = pop_min(a_explorer)
        deja_collectes[courant] = distance 
        
        voisins = {}
        for ami in dico_utilisateurs[courant].amis:
            voisins[ami["id_ami"]] = ami["annees_d_amitie"]
            
        i = 0
        for v in voisins:
            d = distance + dico_utilisateurs[courant].amis[i]["annees_d_amitie"]
            i += 1
            if v not in deja_collectes and d < a_explorer.get(v, math.inf): 
                a_explorer[v] = d 
                
    
    return deja_collectes


print(dijkstra("user1"))


