import re
import json
import os
from typing import List, Dict, Any

class Player:
    """
    Represents a player in the tournament.

    :param name: The name of the player
    :type name: str
    :param first_name: The first name of the player
    :type first_name: str
    :param birth_date: The birth date of the player
    :type birth_date: str
    :param national_id: The national ID of the player
    :type national_id: str
    :return: None
    :rtype: None
    """
    data_file = 'data/players.json'

    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str) -> None:
        """
        Initializes a Player instance.

        :param last_name: Last name of the player
        :type last_name: str
        :param first_name: First name of the player
        :type first_name: str
        :param birth_date: Birth date of the player in format dd/mm/yyyy
        :type birth_date: str
        :param national_id: National ID of the player, two letters followed by five digits (e.g., AB12345)
        :type national_id: str
        :raises ValueError: If the national ID or birth date format is invalid
        :return: None
        :rtype: None
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = 0.0  # Using float for half-points

        # Validate national ID
        if not re.match(r'^[A-Z]{2}\d{5}$', self.national_id):
            raise ValueError("The national ID must be two letters followed by five digits (e.g., AB12345)")

        # Validate birth date format
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', self.birth_date):
            raise ValueError("The birth date must be in the format dd/mm/yyyy")

    def update_points(self, points: float) -> None:
        """
        Updates the player's points.

        :param points: Points to add to the player's total
        :type points: float
        :return: None
        :rtype: None
        """
        self.points += points

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the player instance to a dictionary.

        :return: Dictionary representation of the player
        :rtype: dict
        """
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'national_id': self.national_id,
            'points': self.points
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """
        Creates a Player instance from a dictionary.

        :param data: Dictionary containing player data
        :type data: dict
        :return: Player instance
        :rtype: Player
        """
        player = cls(
            last_name=data['last_name'],
            first_name=data['first_name'],
            birth_date=data['birth_date'],
            national_id=data['national_id']
        )
        player.points = data.get('points', 0.0)
        return player

    @classmethod
    def save_players(cls, player_list: List['Player']) -> None:
        """
        Saves a list of players to a JSON file.

        :param player_list: List of Player instances to save
        :type player_list: list
        :return: None
        :rtype: None
        """
        # Ensure the directory exists, create if not
        directory = os.path.dirname(cls.data_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(cls.data_file, 'w') as f:
            json.dump([player.to_dict() for player in player_list], f, indent=4)

    @classmethod
    def load_players(cls) -> List['Player']:
        """
        Loads a list of players from a JSON file.

        :return: List of Player instances
        :rtype: list
        """
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(player_data) for player_data in data]
        else:
            return []

    def __str__(self) -> str:
        """
        Returns a string representation of the player.

        :return: String representation of the player
        :rtype: str
        """
        return f"{self.last_name} {self.first_name} ({self.national_id})"
