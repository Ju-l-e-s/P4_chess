from datetime import date, datetime
from models.joueur import Joueur
import random


class Tournoi:
    def __init__(self, nom: str, lieu: str, nb_tours: int, joueurs: list, description: str):
        self.nom: str = nom
        self.lieu: str = lieu
        self.date_heure_debut: datetime = datetime.now()
        self.nb_tours: int = nb_tours
        self.tour_actuel: int = 0
        self.joueurs: list = joueurs
        self.tours: list = []
        self.description: str = description

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

    def demarrer_nouveau_tour(self) -> None:
        if self.tour_actuel >= self.nb_tours:
            print("Le tournoi est déjà terminé.")
            return
        self.tour_actuel += 1
        print(f"Tour {self.tour_actuel} démarré.")

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
        return {}


    # Terminer le tournoi
    def terminer(self) -> None:
        self.date_heure_fin = datetime.now()
        print(f"Tournoi terminé à {self.date_heure_fin.strftime('%d/%m/%Y %H:%M')}.")