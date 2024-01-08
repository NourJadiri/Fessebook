import customtkinter as ctk
from tkinter import font

import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

from src.utilisateur import Utilisateur
from src.front.frames.LoginFrame import sc

class UserFrame(ctk.CTkFrame):
    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.user: Utilisateur = user
        self.init_layout()
        self.init_user_info_labels()
        self.init_user_info_values()
        self.init_amis()
        self.init_graphe()

    def init_layout(self):
        # sidebar
        self.grid_columnconfigure(0, weight=1)

        # graphe
        self.grid_columnconfigure(1, weight=4)

        # actions
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(master=self, border_width=2, border_color='white')
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(1, weight=3)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid(row=0, column=0, sticky='nsew')

        self.user_info_frame = ctk.CTkFrame(master=self.sidebar_frame, border_width=2, border_color='white')
        self.user_info_frame.grid(row=0, column=0, sticky='nsew')
        self.user_info_frame.grid_columnconfigure(0, weight=1)

        self.amis_frame = ctk.CTkScrollableFrame(master=self.sidebar_frame, border_width=2, border_color='white', label_text="Amis", label_text_color='pink', label_font=("Helvetica", 20, "bold"))
        self.amis_frame.grid(row=1, column=0, sticky='nsew')
        self.amis_frame.grid_columnconfigure(0, weight=1)

        self.graphe_frame = ctk.CTkFrame(master=self, border_width=2, border_color='white')
        self.graphe_frame.grid(row=0, column=1, sticky='nsew')
        self.graphe_frame.grid_columnconfigure(0, weight=1)
        self.graphe_frame.grid_rowconfigure(0, weight=1)

        self.actions_frame = ctk.CTkFrame(master=self, border_width=2, border_color='white')
        self.actions_frame.grid(row=0, column=2, sticky='nsew')
        self.actions_frame.grid_columnconfigure(0, weight=1)
        self.actions_frame.grid_rowconfigure(0, weight=1)

    def init_user_info_labels(self):
        self.user_info_frame.grid_rowconfigure(0, weight=2)
        self.user_info_frame.grid_rowconfigure(1, weight=1)
        self.user_info_frame.grid_rowconfigure(2, weight=1)
        self.user_info_frame.grid_rowconfigure(3, weight=1)

        self.user_info_frame.grid_columnconfigure(0, weight=1)
        self.user_info_frame.grid_columnconfigure(1, weight=1)

        self.user_info_title = ctk.CTkLabel(master=self.user_info_frame, text="Informations utilisateur",
                                            font=("Helvetica", 18, "bold"), text_color='pink')
        self.user_info_title.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

        self.username_label = ctk.CTkLabel(master=self.user_info_frame, text="Username : ",
                                           font=("Helvetica", 14, "bold"))
        self.username_label.grid(row=1, column=0, sticky='w', padx=10)

        self.full_name_label = ctk.CTkLabel(master=self.user_info_frame, text="Full name : ",
                                            font=("Helvetica", 14, "bold"))
        self.full_name_label.grid(row=2, column=0, sticky='w', padx=10)

        self.age_label = ctk.CTkLabel(master=self.user_info_frame, text="Age : ", font=("Helvetica", 14, "bold"))
        self.age_label.grid(row=3, column=0, sticky='w', padx=10)

    def init_user_info_values(self):
        self.username_value = ctk.CTkLabel(master=self.user_info_frame, text=self.user.user_id, font=("Helvetica", 14))
        self.username_value.grid(row=1, column=1, sticky='w', padx=10)

        self.full_name_value = ctk.CTkLabel(master=self.user_info_frame, text=self.user.nom, font=("Helvetica", 14))
        self.full_name_value.grid(row=2, column=1, sticky='w', padx=10)

        self.age_value = ctk.CTkLabel(master=self.user_info_frame, text=self.user.age, font=("Helvetica", 14))
        self.age_value.grid(row=3, column=1, sticky='w', padx=10)

    def init_amis(self):
        nb_amis = len(self.user.amis)

        for i in range(nb_amis):
            self.amis_frame.grid_rowconfigure(i, weight=1)
            ami_info = self.user.amis[i]
            ami = sc.trouver_utilisateur(ami_info['id_ami'])

            self.ami_label = ctk.CTkLabel(master=self.amis_frame, text=ami.nom, font=("Helvetica", 14))
            self.ami_label.grid(row=i, column=0, sticky='w', padx=10, pady=10)

            self.ami_annees_label = ctk.CTkLabel(master=self.amis_frame, text=ami_info['annees_d_amitie'], font=("Helvetica", 14))
            self.ami_annees_label.grid(row=i, column=1, padx=10, pady=10)

            # add a delete friend button, make it small, and put a x on it
            self.delete_ami_button = ctk.CTkButton(master=self.amis_frame, text="x", height=30, width=30, command=lambda: self.supprimer_ami(ami.user_id))
            self.delete_ami_button.grid(row=i, column=2, padx=10, pady=10)

    def init_actions(self):
        # add a button that displays the graph with the nodes that correspond to dijkstra path
        self.dijkstra_button = ctk.CTkButton(master=self.actions_frame, text="Dijkstra", height=30, command=self.dijkstra)
        self.dijkstra_button.grid(row=0, column=0, pady=(50, 20), padx=20, sticky='ew')

        # add a button that displays the full
        self.full_graph_button = ctk.CTkButton(master=self.actions_frame, text="Full graph", height=30)
        self.full_graph_button.grid(row=1, column=0, pady=(50, 20), padx=20, sticky='ew')

        # add a button that displays the graph with the nodes that correspond to dijkstra path
        self.dijkstra_button = ctk.CTkButton(master=self.actions_frame, text="Dijkstra", height=30)
        self.dijkstra_button.grid(row=0, column=0, pady=(50, 20), padx=20, sticky='ew')



    def init_graphe(self):
        G = sc.construire_graphe()
        pos = nx.spring_layout(G)

        # Dessin des noeuds avec une couleur et une taille spécifiques, la police est en blanc
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color= 'black')

        # Dessin des arêtes avec une largeur et une couleur spécifiques
        edge_labels = {(u, v): d['annees'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edges(G, pos, width=2, edge_color='white')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

        # Ajout des étiquettes (noms d'utilisateurs) aux noeuds du graphe
        labels = {}
        for node in G.nodes():
            labels[node] = node
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='white')

        # Désactivation des axes
        plt.axis('off')

        # Affichage du graphe dans le frame de graphe
        self.fig = plt.gcf()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphe_frame)
        # set dark background
        self.fig.patch.set_facecolor('black')
        self.fig.patch.set_alpha(0.8)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graphe_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)


    def dijkstra(self):
        G = sc.construire_graphe()
        pos = nx.spring_layout(G)

        # Dessin des noeuds avec une couleur et une taille spécifiques, la police est en blanc
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color= 'black')

        # Dessin des arêtes avec une largeur et une couleur spécifiques
        edge_labels = {(u, v): d['annees'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edges(G, pos, width=2, edge_color='white')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

        # Ajout des étiquettes (noms d'utilisateurs) aux noeuds du graphe
        labels = {}
        for node in G.nodes():
            labels[node] = node
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='white')

        # Désactivation des axes
        plt.axis('off')

        # Affichage du graphe dans le frame de graphe
        self.fig = plt.gcf()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphe_frame)
        # set dark background
        self.fig.patch.set_facecolor('black')
        self.fig.patch.set_alpha(0.8)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graphe_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def supprimer_ami(self, ami_id):
        print(sc.session_user)
        sc.supprimer_ami(ami_id)
        for child in self.amis_frame.winfo_children():
            child.destroy()
        self.init_amis()




