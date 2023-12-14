class Utilisateur:
    def __init__(self, user_id, nom, age, activite, amis):
        self.user_id = user_id
        self.nom = nom
        self.age = age
        self.activite = activite
        self.amis = amis

    def __str__(self):
        return (f'Utilisateur: {self.user_id}\n'
                f'\tnom: {self.nom}\n'
                f'\tage: {self.age}\n'
                f'\tactivite: {self.activite}\n'
                f'\tamis: {self.amis}\n')

    def affichage(self):
        print(f'identifiant: {self.user_id}')
        print(f'nom: {self.nom}')
        print(f'age: {self.age}')
        print(f'activite: {self.activite}')
        print(f'amis: {self.amis}')
        print()

    def ajouteramis(self, idamis):
        self.amis.append(idamis)
