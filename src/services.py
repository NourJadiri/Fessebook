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


    def pop_min(self,a_explorer):
        d_min = math.inf
        sommet_min = ""
        for s, d in a_explorer.items():

            if d < d_min:
                d_min = d
                sommet_min = s

        a_explorer.pop(sommet_min)

        return sommet_min, d_min


    def dijkstra(self,depart, dico_utilisateurs):
        a_explorer = {depart: 0}

        for i in dico_utilisateurs:
            if i != depart:
                a_explorer[i] = math.inf

        deja_collectes = {}

        while len(a_explorer) != 0:
            courant, distance = self.pop_min(a_explorer)
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