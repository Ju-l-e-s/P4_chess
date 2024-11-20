from datetime import datetime
from models.round_model import Round
from models.player_model import Player
import json
import os
from typing import List, Dict, Any, Optional, Set, Tuple

class Tournament:
    """
    Represents a tournament.

    :param name: The name of the tournament
    :type name: str
    :param location: The location of the tournament
    :type location: str
    :param start_date: The start date of the tournament, defaults to None
    :type start_date: str, optional
    :param end_date: The end date of the tournament, defaults to None
    :type end_date: str, optional
    :param number_of_rounds: The number of rounds in the tournament
    :type number_of_rounds: int
    :param description: The description of the tournament, defaults to an empty string
    :type description: str, optional
    :param players: The list of players in the tournament, defaults to an empty list
    :type players: list, optional
    :param rounds: The list of rounds in the tournament, defaults to an empty list
    :type rounds: list, optional
    :return: None
    :rtype: None
    """
    data_file = 'data/tournaments.json'

    def __init__(self, name: str, location: str, number_of_rounds: int = 4, description: str = '') -> None:
        """
        Initializes a new tournament.

        :param name: Name of the tournament
        :type name: str
        :param location: Location of the tournament
        :type location: str
        :param number_of_rounds: Number of rounds, defaults to 4
        :type number_of_rounds: int, optional
        :param description: Description of the tournament, defaults to ''
        :type description: str, optional
        :return: None
        :rtype: None
        """
        self.name = name
        self.location = location
        self.start_date = None  # Will be set when the tournament starts
        self.end_date = None
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.players: List[Player] = []
        self.rounds: List[Round] = []
        self.description = description
        self.pairs_already_played: Set[Tuple[str, str]] = set()

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the tournament.

        :param player: Player to add
        :type player: Player
        :return: None
        :rtype: None
        """
        self.players.append(player)

    def add_round(self, round_instance: Round) -> None:
        """
        Adds a round to the tournament.

        :param round_instance: Round to add
        :type round_instance: Round
        :return: None
        :rtype: None
        """
        self.rounds.append(round_instance)
        self.current_round += 1

    def get_ranking(self) -> List[Player]:
        """
        Gets the ranking of players based on their points.

        :return: List of players sorted by points in descending order
        :rtype: List[Player]
        """
        ranking = sorted(self.players, key=lambda player: player.points, reverse=True)
        return ranking

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the tournament to a dictionary.

        :return: Dictionary representation of the tournament
        :rtype: Dict[str, Any]
        """
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'current_round': self.current_round,
            'players': [player.to_dict() for player in self.players],
            'rounds': [round_instance.to_dict() for round_instance in self.rounds],
            'description': self.description,
            'pairs_already_played': list(self.pairs_already_played)
        }

    def end(self) -> None:
        """
        Marks the tournament as finished by setting the end date.

        :return: None
        :rtype: None
        """
        self.end_date = datetime.now().strftime('%d/%m/%Y')

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tournament':
        """
        Creates a Tournament instance from a dictionary.

        :param data: Dictionary containing tournament data
        :type data: Dict[str, Any]
        :return: Tournament instance
        :rtype: Tournament
        """
        tournament = cls(
            name=data['name'],
            location=data['location'],
            number_of_rounds=data.get('number_of_rounds', 4),
            description=data.get('description', '')
        )
        tournament.start_date = data.get('start_date')  # Can be None
        tournament.end_date = data.get('end_date')
        tournament.current_round = data.get('current_round', 0)
        tournament.players = [Player.from_dict(p) for p in data.get('players', [])]
        tournament.rounds = [Round.from_dict(r) for r in data.get('rounds', [])]
        tournament.pairs_already_played = set(tuple(pair) for pair in data.get('pairs_already_played', []))
        return tournament

    @classmethod
    def save_tournaments(cls, tournaments_list: List['Tournament']) -> None:
        """
        Saves a list of tournaments to a JSON file.

        :param tournaments_list: List of tournaments to save
        :type tournaments_list: List[Tournament]
        :return: None
        :rtype: None
        """
        with open(cls.data_file, 'w') as f:
            json.dump([tournament.to_dict() for tournament in tournaments_list], f, indent=4)

    @classmethod
    def load_tournaments(cls) -> List['Tournament']:
        """
        Loads a list of tournaments from a JSON file.

        :return: List of tournaments
        :rtype: List[Tournament]
        """
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(tournament_data) for tournament_data in data]
        else:
            return []
