class Utilisateur:

    def __init__(self, user_id, nom, age, activite, amis, publication):
        self.user_id = user_id
        self.nom = nom
        self.age = age
        self.activite = activite
        self.amis = amis
        self.publication = publication

    # fonction qui permet de représenter un objet sous forme de caractères
    def __str__(self):
        return (f'Utilisateur: {self.user_id}\n'
                f'\tnom: {self.nom}\n'  # \t est une tabulation, 
                f'\tage: {self.age}\n'  # cela permet d'afficher le texte avec une indentation
                f'\tactivite: {self.activite}\n'
                f'\tamis: {self.amis}\n'
                f'\tpublication: {self.publication}\n')

    def affichage(self):
        print(f'identifiant: {self.user_id}')
        print(f'nom: {self.nom}')
        print(f'age: {self.age}')
        print(f'activite: {self.activite}')
        print(f'amis: {self.amis}')
        print(f'publication: {self.publication}')
        print()

    def ajouter_ami(self, id_ami, annees_amitie):
        nouvel_ami = {"id_ami": id_ami, "annees_d_amitie": annees_amitie}
        self.amis.append(nouvel_ami)

    def supprimer_ami(self, id_ami):
        for ami in self.amis:
            if ami['id_ami'] == id_ami:
                self.amis.remove(ami)

    def se_connecter(self):
        self.activite = True

    def se_deconnecter(self):
        self.activite = False

    def poster_publication(self, post):
        self.publication = post
