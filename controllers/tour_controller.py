from models.tour_model import Tour
from controllers.match_controller import MatchController
from models.tournoi_model import Tournoi

import random

class TourController:
    """
    Controller for managing tournament rounds.

    :param tournoi: The tournament instance to manage.
    :type tournoi: Tournoi
    """

    def __init__(self, tournoi: Tournoi):
        """
        Initialize the TourController with a tournament.

        :param tournoi: The tournament instance to manage.
        :type tournoi: Tournoi
        """

    def demarrer_tour(self, round_number: int) -> None:
        """
        Start a new round in the tournament.

        :param round_number: The number of the round to start.
        :type round_number: int
        """
    def __init__(self, tournoi):
        self.tournoi = tournoi

    def demarrer_tour(self,round_number):
        def demarrer_tour(self, round_number: int) -> None:
            """
            Démarre un nouveau tour du tournoi.

            :param round_number: Le numéro du tour à démarrer.
            :type round_number: int
            :return: None
            :rtype: None
            """
        tour = Tour(f"Round {round_number}")
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
