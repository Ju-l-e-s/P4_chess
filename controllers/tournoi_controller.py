from models.tournoi_model import Tournoi
from models.joueur_model import Joueur
from controllers.tour_controller import TourController
from views.tournoi_view import TournoiView
from controllers.joueur_controller import JoueurController

from datetime import datetime


class TournoiController:
    def __init__(self):
        self.tournois = Tournoi.charger_tournois()
        self.joueur_controller = JoueurController()

    def creer_tournoi(self):
        # Création du tournoi
        nom, lieu, nb_tours, description = TournoiView.demander_informations_tournoi()
        tournoi = Tournoi(nom, lieu, int(nb_tours), description)

        # Ajout des joueurs au tournoi
        print("\n--- Ajout des joueurs au tournoi ---")

        joueurs_disponibles = self.joueur_controller.joueurs
        if not joueurs_disponibles:
            print("Aucun joueur disponible pour ce tournoi.")
            return

        # Affichage des joueurs avec des numéros pour la sélection
        for index, joueur in enumerate(joueurs_disponibles, start=1):
            print(f"{index}. {joueur.nom} {joueur.prenom} (ID: {joueur.id_national})")

        # Boucle pour permettre la sélection de plusieurs joueurs
        joueurs_ajoutes = set()  # Pour éviter les doublons
        while True:
            choix = input("Entrez le(s) numéro(s) des joueurs à ajouter (ex: 1,3,5 ou 'fin' pour terminer) : ")
            if choix.lower() == 'fin':
                break

            try:
                # Diviser la chaîne de caractères par les virgules, et convertir chaque partie en un index
                indices = [int(num.strip()) - 1 for num in choix.split(',')]
                for index in indices:
                    if 0 <= index < len(joueurs_disponibles):
                        joueur = joueurs_disponibles[index]
                        if joueur not in joueurs_ajoutes:
                            tournoi.ajouter_joueur(joueur)
                            joueurs_ajoutes.add(joueur)
                            print(f"Joueur {joueur.nom} {joueur.prenom} ajouté au tournoi.")
                        else:
                            print(f"Joueur {joueur.nom} {joueur.prenom} déjà ajouté au tournoi.")
                    else:
                        print(f"Le numéro {index + 1} est invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des numéros séparés par des virgules.")

        # Finalisation de la création du tournoi
        self.tournois.append(tournoi)
        Tournoi.sauvegarder_tournois(self.tournois)
        print("Tournoi créé avec succès.")

    def demarrer_tournoi(self, tournoi):
        tours_restants = tournoi.nb_tours - tournoi.tour_actuel
        for _ in range(tours_restants):
            tour_controller = TourController(tournoi)
            tour_controller.demarrer_tour()
            # Incrémentation du tour actuel si nécessaire
            # tournoi.tour_actuel += 1  # Décommenter si l'incrémentation ne se fait pas ailleurs
            Tournoi.sauvegarder_tournois(self.tournois)
        # Le tournoi est terminé
        tournoi.terminer()
        Tournoi.sauvegarder_tournois(self.tournois)
        classement = tournoi.get_classement()
        TournoiView.afficher_classement(classement)



    def lister_tournois(self):
        self.tournois = Tournoi.charger_tournois()
        TournoiView.afficher_liste_tournois(self.tournois)

    def selectionner_tournoi(self):
        # Filtrer les tournois pour n'afficher que ceux qui n'ont pas encore de date de fin
        tournois_en_cours = [tournoi for tournoi in self.tournois if not tournoi.date_fin]
        if not tournois_en_cours:
            print("Aucun tournoi en cours disponible.")
            return None

        print("\n--- Liste des tournois disponibles ---")
        for index, tournoi in enumerate(tournois_en_cours, start=1):
            # Convertir en datetime si `date_debut` est une chaîne
            date_debut = datetime.strptime(tournoi.date_debut, "%d/%m/%Y") if isinstance(tournoi.date_debut,
                                                                                         str) else tournoi.date_debut
            date_fin = "En cours"  # Affichage pour les tournois en cours

            # Affichage formaté
            date_debut_str = date_debut.strftime("%d/%m/%Y") if date_debut else "Non défini"
            print(f"{index}. {tournoi.nom} à débuté le {date_debut_str} (à {tournoi.lieu}) ")

        while True:
            choix = input("Entrez le numéro du tournoi à sélectionner (ou 'retour' pour revenir au menu principal) : ")
            if choix.lower() == 'retour':
                return None  # Permet de revenir au menu principal

            try:
                index = int(choix) - 1
                if 0 <= index < len(tournois_en_cours):
                    return tournois_en_cours[index]
                else:
                    print("Choix invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")
    def afficher_details_tournoi(self, tournoi):
        TournoiView.afficher_informations_tournoi(tournoi)
        TournoiView.afficher_classement(tournoi.get_classement())