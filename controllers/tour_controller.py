from models.tour_model import Tour
from controllers.match_controller import MatchController

import random

class TourController:
    def __init__(self, tournoi):
        self.tournoi = tournoi

    def demarrer_tour(self):
        tour = Tour(f"Round {self.tournoi.tour_actuel + 1}")
        if self.tournoi.tour_actuel == 0:
            # Premier tour : mélanger les joueurs
            joueurs = self.tournoi.joueurs.copy()
            random.shuffle(joueurs)
        else:
            # Tours suivants : trier par points
            joueurs = sorted(self.tournoi.joueurs, key=lambda j: (-j.points, j.nom))
        # Créer les matchs
        tour.creer_matchs(joueurs, self.tournoi.paires_deja_jouees)
        self.tournoi.ajouter_tour(tour)
        # Gérer les matchs
        for match in tour.matchs:
            match_controller = MatchController(match)
            match_controller.jouer_match()
            # Enregistrer les paires jouées
            paire = (match.joueur1.id_national, match.joueur2.id_national)
            self.tournoi.paires_deja_jouees.add(paire)
        tour.terminer(self.tournoi)
