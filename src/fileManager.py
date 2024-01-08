from src.utilisateur import Utilisateur
import json  # Bibliothèque pour la manipulation de fichiers JSON


class FileManager:
    userFile = "../data/users_linked.json"
    publicationsFile = "../data/publications.json"

    users_donnees = None
    publications_donnees = None

    def __init__(self):
        with open(FileManager.userFile, 'r') as file:
            FileManager.users_donnees = json.load(file)

        with open(FileManager.publicationsFile, 'r') as file:
            FileManager.publications_donnees = json.load(file)

        pass

    def initialiser_dico_utilisateurs_json(self):
        dico_users = {}

        for utilisateur in self.users_donnees:
            user = Utilisateur(
                utilisateur['username'], utilisateur['full_name'],
                utilisateur['age'], utilisateur['is_active'], utilisateur['amis'],
                "")  # les derniers guillemets correspondent
            # à l'attribut publication qui n'est pas présent
            dico_users[utilisateur['username']] = user  # dans le fichier json

        return dico_users

    def initialiser_dico_publications_json(self):
        dico_publications = {}

        for publication in self.publications_donnees:
            dico_publications[publication['id']] = publication

        return dico_publications

    def ajouter_ami(self, id_user, id_ami, annees_amitie):
        for user in self.users_donnees:
            if user['username'] == id_user:
                nouvel_ami = {"id_ami": id_ami, "annees_d_amitie": annees_amitie}
                user['amis'].append(nouvel_ami)
                break

        for user in self.users_donnees:
            if user['username'] == id_ami:
                nouvel_ami = {"id_ami": id_user, "annees_d_amitie": annees_amitie}
                user['amis'].append(nouvel_ami)
                break

        print(self.users_donnees)

        with open(self.userFile, 'w') as file:
            if self.users_donnees is not None:
                json.dump(self.users_donnees, file, indent=4)

    def supprimer_ami(self, id_user, id_ami):

        for user in self.users_donnees:
            if user['username'] == id_user:
                user['amis'] = [ami for ami in user['amis'] if ami['id_ami'] != id_ami]
            if user['username'] == id_ami:
                user['amis'] = [ami for ami in user['amis'] if ami['id_ami'] != id_user]

        with open(self.userFile, 'w') as file:
            json.dump(self.users_donnees, file, indent=4)

    def trouver_utilisateur(self, id_user, mot_de_passe):

        for user in self.users_donnees:
            if user['username'] == id_user and user['password'] == mot_de_passe:
                return user
        return None
