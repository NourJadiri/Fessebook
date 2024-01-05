from utilisateur import Utilisateur 
import json  # Bibliothèque pour la manipulation de fichiers JSON

fichier = "users_linked.json"


# Fonction pour initialiser la liste d'utilisateurs à partir d'un fichier JSON
def initialiser_dico_utilisateurs_json(file_path):
    with open(file_path, 'r') as file:
        donnees = json.load(file)
        
#    donnees renvoie : 
#    [{'username': 'user1', 'full_name': 'David Wilson', 'age': 57, 'is_active': True, 
#    'amis': [{'user_id': 'user3', "annees d'amitie": 30}, 
#    {'user_id': 'user98', "annees d'amitie": 20}, {'user_id': 'user29', "annees d'amitie": 10}, 
#    {'user_id': 'user4', "annees d'amitie": 15}, {'user_id': 'user11', "annees d'amitie": 5}]},
    
    dico_users = {}
    
    for utilisateur in donnees:
        user = Utilisateur(
            utilisateur['username'], utilisateur['full_name'], 
            utilisateur['age'], utilisateur['is_active'], utilisateur['amis'], "") # les derniers guillemets correspondent 
                                                                                   # à l'attribut publication qui n'est pas présent
        dico_users[utilisateur['username']] = user                                 # dans le fichier json
        
    return dico_users


#print(initialiser_dico_utilisateurs_json(fichier))  # {'user1' : objet1, 'user2' : ...}
#print()

dico_utilisateurs = initialiser_dico_utilisateurs_json(fichier)




# fonctions pour directement ajouter/supprimer des amis dans les 2 sens

def ajouter_ami2sens(id_user, id_ami , annees_amitie, dico):
    
     dico[id_user].ajouter_amis(id_ami , annees_amitie)
     dico[id_ami].ajouter_amis(id_user, annees_amitie)
     
     
def supprimer_ami2sens(id_user, id_ami, dico):
     
    dico[id_user].supprimer_ami(id_ami)
    dico[id_ami].supprimer_ami(id_user)
    
    
# affiche le profil d'un ami de user
def afficher_profil_ami(user, id_ami, dico):
    affichage = False
    for ami in dico[user].amis:
        if ami['id_ami'] == id_ami :
            dico[id_ami].affichage()
            affichage = True
    if affichage == False:
        print(f"Aucun utilisateur trouvé avec l'identifiant {id_ami}")
    
   


def creer_profil(nom, age, activite, amis, dico_utilisateurs):
    
    nouveau_user_id = "user"  + str(len(dico_utilisateurs)+1)
    
    #partie pour avoir un nom d'utilisateur unique 
    for user in dico_utilisateurs:
        if user == nouveau_user_id:     
            
            nouveau_user_id = user + "1"
    publication = ""
    nouveau_utilisateur = Utilisateur(nouveau_user_id, nom, age, activite, amis, publication)
    
    dico_utilisateurs[nouveau_user_id] = nouveau_utilisateur
    for ami in amis:
        
        dico_utilisateurs[ami['id_ami']].ajouter_amis(nouveau_user_id, ami['annees_d_amitie'])
        
    return nouveau_user_id


def supprimer_profil(user, dico_utilisateurs):
    
    for ami in dico_utilisateurs[user].amis:
        dico_utilisateurs[ami['id_ami']].supprimer_ami(user)
        
    dico_utilisateurs.pop(user)


   
#%%
    
# TEST des nouvelles fonctions            
mot  = [0, 6, 7, 99]


for numéro in mot: 
    
    if numéro == 0:
        for o in dico_utilisateurs.values():
           	o.affichage()
        print()
    
    if numéro == 1:
        supprimer_ami2sens('user1', 'user9', dico_utilisateurs)
        print()
    
    if numéro == 2:
        ajouter_ami2sens('user1', 'user9', 22, dico_utilisateurs)
        print()

    if numéro == 3:
        dico_utilisateurs['user7'].se_connecter_deconnecter("connexion")
        print()
        
    if numéro == 4:
         dico_utilisateurs['user10'].poster_publication("Vive le chocolat")
         print()
         
    if numéro == 5:
         afficher_profil_ami('user10', 'user6', dico_utilisateurs)
         print()
         
    if numéro == 6:  
        creer_profil("Jackie Chan", 25, True, [{'id_ami': 'user8', 'annees_d_amitie': 10},{'id_ami': 'user7', 'annees_d_amitie': 13}], dico_utilisateurs)
        print()
    
    if numéro == 7:
         supprimer_profil('user9', dico_utilisateurs)
         print()
    
    if numéro == 99:
        for o in dico_utilisateurs.values():
           	o.affichage()
        print()
            

     


       




