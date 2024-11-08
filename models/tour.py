from datetime import datetime
from models.tournoi import Tournoi
from models.match import Match

import random

class Tour:
    def __init__(self, nom: str, date_heure_debut: str):
        self.nom: str = nom
        self.date_heure_debut: datetime = datetime.now()
        # self.date_heure_fin: datetime = self.convertir_date(date_heure_fin)
        self.matchs: list = self.creer_matchs()

   
    
    def afficher_informations(self) -> None:
        date_heure_debut_str = self.date_heure_debut.strftime("%d/%m/%Y %H:%M")
        date_heure_fin_str = self.date_heure_fin.strftime("%d/%m/%Y %H:%M")
        liste_matchs = ', '.join(str(match) for match in self.matchs)
        print(f"Nom: {self.nom}, Date et heure de début: {date_heure_debut_str}, Date et heure de fin: {date_heure_fin_str}, Matchs: [{liste_matchs}]")
    
    def creer_matchs(self, liste_joueurs):
        # 1. Mélanger ou trier les joueurs selon le tour
        if self.nom == "Round 1":  # Exemple : mélanger pour le premier tour
            random.shuffle(liste_joueurs)
        else:  # Pour les tours suivants, trier les joueurs par score
            liste_joueurs.sort(key=lambda joueur: joueur.points, reverse=True)

        # 2. Appairer les joueurs pour créer des matchs
        self.matchs = []  # Initialise la liste des matchs pour le tour
        for i in range(0, len(liste_joueurs), 2):
            joueur1 = liste_joueurs[i]
            joueur2 = liste_joueurs[i + 1] if i + 1 < len(liste_joueurs) else None  # Gestion du cas impair

            if joueur2:
                # Créer un match entre joueur1 et joueur2
                match = Match(joueur1, joueur2)
                self.matchs.append(match)
                print(f"Match créé : {joueur1} vs {joueur2}")
            else:
                # Si le nombre de joueurs est impair, joueur1 n'a pas d'adversaire pour ce tour
                print(f"{joueur1} n'a pas d'adversaire pour ce tour.")

        # 3. Retourne la liste des matchs (optionnel)
        return self.matchs
        
    # Terminer le tour
    def terminer(self) -> None:
        self.date_heure_fin = datetime.now()
        print(f"Tour terminé à {self.date_heure_fin.strftime('%d/%m/%Y %H:%M')}.")
        
    # Logique pour vérifier si le tournoi est terminé
    # Préparation de la liste de joueurs (triée ou mélangée)
    # Création d'une instance de Tour
    # Appel à tour.creer_matchs(liste_joueurs)
    # Ajout du tour à self.tours et incrémentation de self.tour_actuel
    def demarrer_nouveau_tour(self) -> None:
        # Vérification si le tournoi est terminé
        if self.tour_actuel > self.nb_tours:
            print("Le tournoi est terminé.")
            return
        Tournoi.demarrer_nouveau_tour()

        # Préparation de la liste de joueurs (triée ou mélangée)
        liste_joueurs = self.liste_joueurs_aléatoire()

        # Création d'une instance de Tour
        tour = Tour(f"Round {self.tour_actuel}", datetime.now())
        # Appel à tour.creer_matchs(liste_joueurs)
        tour.creer_matchs(liste_joueurs)

        # Ajout du tour à self.tours et incrémentation de self.tour_actuel
        self.tours.append(tour)
        self.tour_actuel += 1

        print(f"Tour {self.tour_actuel - 1} démarré.")