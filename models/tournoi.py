from datetime import date, datetime
from models.joueur import Joueur
from models.tour import Tour
from models.match import Match
import json
import os
import random


class Tournoi:
    def __init__(self, nom: str, lieu: str, date_debut: str, date_fin: str, nb_tours: int, tour_actuel: int, tours: int, joueurs: list, description: str):
        self.nom: str = nom
        self.lieu: str = lieu
        self.date_debut: date = self.convertir_date(date_debut)
        self.date_fin: date = self.convertir_date(date_fin)
        self.nb_tours: int = nb_tours
        self.tour_actuel: int = 0  # Initialisé à 0 au départ
        self.joueurs: list = joueurs
        self.tours: list = []
        self.description: str = description

    def ajouter_tour(self):
        from models.tour import Tour  # Import local pour éviter le circular import
        nouveau_tour = Tour(...)  # Initialisation de Tour si nécessaire
        self.tours.append(nouveau_tour)

    def convertir_date(self, date_str: str) -> date:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("La date doit être au format jj/mm/aaaa")

    def afficher_informations(self) -> None:
        date_debut_str = self.date_debut.strftime("%d/%m/%Y")
        date_fin_str = self.date_fin.strftime("%d/%m/%Y")
        liste_joueurs = ', '.join(str(joueur) for joueur in self.joueurs)
        print(f"Nom: {self.nom}, Lieu: {self.lieu}, Date de début: {date_debut_str}, Date de fin: {date_fin_str}, Nombre de tours: {self.nb_tours}, Tour actuel: {self.tour_actuel}, Joueurs: [{liste_joueurs}], Tours: {self.tours}")

    def ajouter_joueur(self, joueur: Joueur) -> None:
        self.joueurs.append(joueur)

    # afficher la liste des joueurs par ordre alphabétique

    def afficher_joueurs_par_ordre_alphabetique(self) -> list:
        liste_joueurs = []
        self.joueurs.sort(key=lambda joueur: joueur.nom)
        for joueur in self.joueurs:
            print(joueur)
            liste_joueurs.append(joueur)

    def liste_joueurs_aléatoire(self) -> list:
        liste_joueurs = []
        for joueur in self.joueurs:
            liste_joueurs.append(joueur)
        random.shuffle(liste_joueurs)  # Ne pas assigner le résultat
        return liste_joueurs  # Retourner la liste mélangée

    def obtenir_rapport(self) -> dict:
        # Logique pour obtenir le rapport du tournoi

        return {

        }

    def demarrer_nouveau_tour(self) -> None:
        from models.tour import Tour  # Import local pour éviter l'import circulaire

        # Vérification si le tournoi est terminé
        if self.tour_actuel >= self.nb_tours:
            print("Le tournoi est terminé.")
            return

        print(f"\n--- Début du Tour {self.tour_actuel + 1} ---")

        # Création d'une instance de Tour
        tour = Tour(f"Round {self.tour_actuel + 1}")

        # Préparation de la liste de joueurs (triée ou mélangée)
        if self.tour_actuel == 0:
            # Pour le premier tour, mélanger les joueurs
            liste_joueurs = self.liste_joueurs_aléatoire()
        else:
            # Pour les tours suivants, trier les joueurs par points
            self.joueurs.sort(key=lambda joueur: joueur.points, reverse=True)
            liste_joueurs = self.joueurs.copy()

        # Initialiser paires_deja_jouees si elle n'existe pas
        if not hasattr(self, 'paires_deja_jouees'):
            self.paires_deja_jouees = set()

        # Créer les matchs pour le tour
        tour.creer_matchs(liste_joueurs, self.paires_deja_jouees)

        # Ajouter le tour à la liste des tours du tournoi
        self.tours.append(tour)

        # Incrémenter le compteur de tours
        self.tour_actuel += 1


    def sauvegarder_tournoi(self, chemin_fichier):
        """Sauvegarde le tournoi dans un fichier JSON."""
        print(f"Tentative de sauvegarde du tournoi dans {chemin_fichier}")
        
        # Vérifier que le dossier existe, sinon le créer
        dossier = os.path.dirname(chemin_fichier)
        if dossier and not os.path.exists(dossier):
            print(f"Le dossier {dossier} n'existe pas. Création du dossier.")
            os.makedirs(dossier)
        else:
            print(f"Le dossier {dossier} existe déjà.")
        
        # Sauvegarder le tournoi en JSON
        try:
            with open(chemin_fichier, "w") as fichier:
                json.dump(self.to_dict(), fichier, indent=4)
            print(f"Tournoi sauvegardé avec succès dans {chemin_fichier}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du tournoi : {e}")


    def to_dict(self):
        """Convertit l'instance de Tournoi en dictionnaire, incluant les joueurs et les tours."""
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut.strftime('%d/%m/%Y %H:%M:%S'),
            "date_fin": self.date_fin.strftime('%d/%m/%Y %H:%M:%S'),
            "nb_tours": self.nb_tours,
            "tour_actuel": self.tour_actuel,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs],
            "tours": [tour.to_dict() for tour in self.tours],
            "description": self.description
        }
    # Terminer le tournoi
    def afficher_classement(self) -> None:
        # Trier les joueurs par points (et par nom en cas d'égalité)
        classement = sorted(self.joueurs, key=lambda joueur: (-joueur.points, joueur.nom))
        
        print("\n--- Classement des Joueurs ---")
        for i, joueur in enumerate(classement, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} - {joueur.points} points")
    def terminer(self) -> None:
        self.date_heure_fin = datetime.now()
        print(f"Tournoi terminé à {self.date_heure_fin.strftime('%d/%m/%Y %H:%M')}.")

    @classmethod
    def charger_tournoi(cls, chemin):
        """Charge le tournoi depuis un fichier JSON."""
        with open(chemin, "r") as fichier:
            data = json.load(fichier)
            return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Tournoi à partir d'un dictionnaire, incluant les joueurs et les tours."""
        tournoi = cls(
            nom=data["nom"],
            lieu=data["lieu"],
            date_debut=data["date_debut"],
            date_fin=data["date_fin"],
            nb_tours=data["nb_tours"],
            joueurs=[Joueur.from_dict(j) for j in data["joueurs"]],
            description=data["description"]
        )
        tournoi.date_debut = datetime.strptime(data["date_debut"], '%d/%m/%Y').date()
        tournoi.date_fin = datetime.strptime(data["date_fin"], '%d/%m/%Y').date()
        tournoi.tour_actuel = data.get("tour_actuel", 0)
        tournoi.tours = [Tour.from_dict(t) for t in data.get("tours", [])]
        return tournoi
