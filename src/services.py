import networkx as nx
import math
from fileManager import FileManager
from src.utilisateur import Utilisateur


class Service:
    users_dico = None
    publications_dico = None
    session_user = None
    fm = FileManager()

    def __init__(self):
        self.users_dico = self.fm.initialiser_dico_utilisateurs_json()

    def login(self, id_user, mot_de_passe):
        user_json = self.fm.trouver_utilisateur(id_user, mot_de_passe)
        if user_json is not None:
            self.session_user = Utilisateur(user_json['username'], user_json['full_name'], user_json['age'],
                                            user_json['is_active'], user_json['amis'], [])
            return True
        return False

    def trouver_utilisateur(self, id_user):
        return self.users_dico[id_user]

    def supprimer_ami(self, id_ami):
        self.session_user.supprimer_ami(id_ami)
        self.fm.supprimer_ami(self.session_user.user_id, id_ami)

    def construire_graphe(self):
        G = nx.Graph()
        for utilisateur in self.users_dico.values():
            for ami in utilisateur.amis:
                G.add_edge(utilisateur.user_id, ami["id_ami"], annees=ami["annees_d_amitie"])
        return G

    def pop_min(self, a_explorer):
        min = math.inf
        for i in a_explorer:
            if a_explorer[i] < min:
                min = a_explorer[i]
                cle_min = i
        a_explorer.pop(cle_min)
        return cle_min, min

    def dijkstra(self, depart):
        G = self.construire_graphe()
        a_explorer = {}
        deja_explore = {}
        predecesseur = {}
        for i in G.nodes:
            a_explorer[i] = math.inf
        a_explorer[depart] = 0
        while a_explorer:
            u, d = self.pop_min(a_explorer)
            deja_explore[u] = d
            for v in G.neighbors(u):
                if v not in deja_explore:
                    if a_explorer[v] > deja_explore[u] + G.edges[u, v]['annees']:
                        a_explorer[v] = deja_explore[u] + G.edges[u, v]['annees']
                        predecesseur[v] = u
        return predecesseur, deja_explore
