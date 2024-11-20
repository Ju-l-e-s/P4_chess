# models/tournoi.py

from datetime import datetime
from models.tour_model import Tour
from models.joueur_model import Joueur
import json
import os
from typing import List, Dict, Any, Optional, Set, Tuple

class Tournoi:
    data_file = 'data/tournois.json'

    def __init__(self, nom: str, lieu: str, nb_tours: int = 4, description: str = '') -> None:
        """
        Initialize a new tournament.

        :param nom: Name of the tournament
        :type nom: str
        :param lieu: Location of the tournament
        :type lieu: str
        :param nb_tours: Number of rounds, defaults to 4
        :type nb_tours: int, optional
        :param description: Description of the tournament, defaults to ''
        :type description: str, optional
        """
        self.nom = nom
        self.lieu = lieu
        self.date_debut = datetime.now().strftime('%d/%m/%Y')  # Current date
        self.date_fin = None  # Will be set at the end of the tournament
        self.nb_tours = nb_tours
        self.tour_actuel = 0
        self.joueurs = []
        self.tours = []
        self.description = description
        self.paires_deja_jouees = set()

    def ajouter_joueur(self, joueur: Joueur) -> None:
        """
        Add a player to the tournament.

        :param joueur: Player to add
        :type joueur: Joueur
        """
        self.joueurs.append(joueur)

    def ajouter_tour(self, tour: Tour) -> None:
        """
        Add a round to the tournament.

        :param tour: Round to add
        :type tour: Tour
        """
        self.tours.append(tour)
        self.tour_actuel += 1
        
    def get_classement(self) -> List[Joueur]:
        """
        Get the ranking of players based on their points.

        :return: List of players sorted by points in descending order
        :rtype: List[Joueur]
        """
        classement = sorted(self.joueurs, key=lambda joueur: joueur.points, reverse=True)
        return classement
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the tournament to a dictionary.

        :return: Dictionary representation of the tournament
        :rtype: Dict[str, Any]
        """
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'nb_tours': self.nb_tours,
            'tour_actuel': self.tour_actuel,
            'joueurs': [joueur.to_dict() for joueur in self.joueurs],
            'tours': [tour.to_dict() for tour in self.tours],
            'description': self.description,
            'paires_deja_jouees': list(self.paires_deja_jouees)
        }
        
    def terminer(self) -> None:
        """
        Mark the tournament as finished by setting the end date.
        """
        self.date_fin = datetime.now().strftime('%d/%m/%Y')
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tournoi':
        """
        Create a tournament instance from a dictionary.

        :param data: Dictionary containing tournament data
        :type data: Dict[str, Any]
        :return: Tournament instance
        :rtype: Tournoi
        """
        tournoi = cls(
            nom=data['nom'],
            lieu=data['lieu'],
            nb_tours=data.get('nb_tours', 4),
            description=data.get('description', '')
        )
        tournoi.date_debut = data['date_debut']
        tournoi.date_fin = data.get('date_fin')  # Can be None
        tournoi.tour_actuel = data.get('tour_actuel', 0)
        tournoi.joueurs = [Joueur.from_dict(j) for j in data.get('joueurs', [])]
        tournoi.tours = [Tour.from_dict(t) for t in data.get('tours', [])]
        tournoi.paires_deja_jouees = set(tuple(paire) for paire in data.get('paires_deja_jouees', []))
        return tournoi

    @classmethod
    def sauvegarder_tournois(cls, liste_tournois: List['Tournoi']) -> None:
        """
        Save a list of tournaments to a JSON file.

        :param liste_tournois: List of tournaments to save
        :type liste_tournois: List[Tournoi]
        """
        with open(cls.data_file, 'w') as f:
            json.dump([tournoi.to_dict() for tournoi in liste_tournois], f, indent=4)

    @classmethod
    def charger_tournois(cls) -> List['Tournoi']:
        """
        Load a list of tournaments from a JSON file.

        :return: List of tournaments
        :rtype: List[Tournoi]
        """
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(tournoi_data) for tournoi_data in data]
        else:
            return []
