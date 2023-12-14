from src.utilisateur import Utilisateur


def parse_user_data(line):
    # Cette fonction prend une ligne de texte en entrée, la divise en plusieurs parties,
    # convertit les données nécessaires et crée un nouvel objet Utilisateur avec ces données.
    # Elle retourne ensuite cet objet Utilisateur.

    data = line.strip().split(',')

    user_id = data[0]
    full_name = data[1]
    age = int(data[2])
    is_active = (data[3] == "True")
    related_users = data[4:]

    return Utilisateur(user_id, full_name, age, is_active, related_users)


def initialiser_liste_utilisateurs(file):
    # Cette fonction ouvre un fichier donné, lit chaque ligne, utilise la fonction parse_user_data
    # pour convertir chaque ligne en un objet Utilisateur, puis ajoute cet objet à une liste.
    # Elle retourne ensuite cette liste d'objets Utilisateur.

    dico_utilisateurs = {}
    with open(file, "r") as fichier:
        for line in fichier:
            user = parse_user_data(line)
            dico_utilisateurs[user.user_id] = user
    return dico_utilisateurs
