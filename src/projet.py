#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:41:58 2023

@author: awidmer
"""

import networkx as nx
import matplotlib.pyplot as plt
import fileManager as fm


def main():
    G = nx.Graph()

    dico_utilisateurs = fm.initialiser_liste_utilisateurs('users.txt')

    for utilisateur in dico_utilisateurs.values():
        for ami in utilisateur.amis:
            G.add_edge(utilisateur.user_id, ami)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='blue')

    labels = {}
    for node in G.nodes():
        labels[node] = node
    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
