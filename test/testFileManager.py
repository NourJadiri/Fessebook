import json

from src.fileManager import FileManager

fm = FileManager()


def test_initialiser_dico_utilisateurs_json():
    dico_users = fm.initialiser_dico_utilisateurs_json()

    for value in dico_users.values():
        print(value)


def test_ajouter_ami():
    fm.ajouter_ami('user1', 'user2', 3)


def test_supprimer_ami():
    fm.supprimer_ami('user1', 'user2')


def test_trouver_utilisateur():
    user = fm.trouver_utilisateur('user1', 'password1')
    print(user)

test_trouver_utilisateur()
