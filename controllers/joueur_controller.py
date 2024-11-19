# controllers/joueur_controller.py

from models.joueur_model import Joueur
from views.joueur_view import JoueurView

class JoueurController:
    def __init__(self):
        self.joueurs = Joueur.charger_joueurs()

    def ajouter_joueur(self):
        while True:
            try:
                nom, prenom, date_naissance, id_national = JoueurView.demander_informations_joueur()
                joueur = Joueur(nom, prenom, date_naissance, id_national)
                self.joueurs.append(joueur)
                Joueur.sauvegarder_joueurs(self.joueurs)
                print("Joueur ajouté avec succès.")
                break  # Sortir de la boucle si tout va bien
            except ValueError as e:
                print(f"Erreur : {e}")
                print("Veuillez réessayer.")

    def lister_joueurs(self):
        self.joueurs = Joueur.charger_joueurs()
        self.joueurs.sort(key=lambda j: j.nom)
        JoueurView.afficher_joueurs(self.joueurs)
        
    def lister_joueurs_alphabetique(self):
        self.joueurs = Joueur.charger_joueurs()
        self.joueurs.sort(key=lambda j: (j.nom, j.prenom))
        JoueurView.afficher_joueurs(self.joueurs)