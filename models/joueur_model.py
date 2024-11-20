# models/joueur.py

import re
import json
import os
from typing import List, Dict, Any

class Joueur:
    data_file = 'data/joueurs.json'

    def __init__(self, nom: str, prenom: str, date_naissance: str, id_national: str) -> None:
        """
        Initialize a Joueur instance.

        :param nom: Last name of the player
        :type nom: str
        :param prenom: First name of the player
        :type prenom: str
        :param date_naissance: Birth date of the player in the format dd/mm/yyyy
        :type date_naissance: str
        :param id_national: National ID of the player, must be two letters followed by five digits (e.g., AB12345)
        :type id_national: str
        :raises ValueError: If the national ID or birth date format is invalid
        """
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_national = id_national
        self.points = 0.0  # Using float for half-points

        # Validate national ID
        if not re.match(r'^[A-Z]{2}\d{5}$', self.id_national):
            raise ValueError("The national ID must be two letters followed by five digits (e.g., AB12345)")

        # Validate birth date format
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', self.date_naissance):
            raise ValueError("The birth date must be in the format dd/mm/yyyy")
    
    def mettre_a_jour_points(self, points: float) -> None:
        """
        Update the player's points.

        :param points: Points to add to the player's total
        :type points: float
        """
        self.points += points
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the player instance to a dictionary.

        :return: Dictionary representation of the player
        :rtype: dict
        """
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'id_national': self.id_national,
            'points': self.points
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Joueur':
        """
        Create a Joueur instance from a dictionary.

        :param data: Dictionary containing player data
        :type data: dict
        :return: Joueur instance
        :rtype: Joueur
        """
        joueur = cls(
            nom=data['nom'],
            prenom=data['prenom'],
            date_naissance=data['date_naissance'],
            id_national=data['id_national']
        )
        joueur.points = data.get('points', 0.0)
        return joueur

    @classmethod
    def sauvegarder_joueurs(cls, liste_joueurs: List['Joueur']) -> None:
        """
        Save a list of players to a JSON file.

        :param liste_joueurs: List of Joueur instances to save
        :type liste_joueurs: list
        """
        # Ensure the directory exists, create if not
        directory = os.path.dirname(cls.data_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(cls.data_file, 'w') as f:
            json.dump([joueur.to_dict() for joueur in liste_joueurs], f, indent=4)

    @classmethod
    def charger_joueurs(cls) -> List['Joueur']:
        """
        Load a list of players from a JSON file.

        :return: List of Joueur instances
        :rtype: list
        """
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(joueur_data) for joueur_data in data]
        else:
            return []

    def __str__(self) -> str:
        """
        Return a string representation of the player.

        :return: String representation of the player
        :rtype: str
        """
        return f"{self.nom} {self.prenom} ({self.id_national})"
