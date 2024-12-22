from datetime import datetime
from models.player_model import Player
from typing import List, Set, Tuple, Dict, Any, Optional


class Round:
    """
    Represents a round in the tournament.

    :param name: The name of the round
    :type name: str
    :param matches: The list of matches in the round, defaults to an empty list
    :type matches: list, optional
    :param start_datetime: The start datetime of the round, defaults to the current datetime
    :type start_datetime: datetime, optional
    :param end_datetime: The end datetime of the round, defaults to None
    :type end_datetime: datetime, optional
    :return: None
    :rtype: None
    """

    def __init__(self, name: str, number: int) -> None:
        """
        Initializes a Round instance.

        :param name: The name of the round.
        :type name: str
        :param number: The number of the round.
        :type number: int
        :return: None
        :rtype: None
        """
        self.name: str = name
        self.number: int = number  # Added number to track round number
        self.start_datetime: datetime = datetime.now()
        self.end_datetime: Optional[datetime] = None
        self.matches: List[Tuple[List[Any], List[Any]]] = []

    def display_info(self) -> None:
        """
        Displays the round's information.

        :return: None
        :rtype: None
        """
        start_str = self.start_datetime.strftime("%d/%m/%Y %H:%M")
        end_str = self.end_datetime.strftime(
            "%d/%m/%Y %H:%M") if self.end_datetime else "En cours"
        print(f"{self.name} - Début: {start_str}, Fin: {end_str}")

    def end(self, tournament) -> None:
        """
        Ends the round and updates the tournament's status.

        :param tournament: The tournament instance.
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        self.end_datetime = datetime.now()
        print(f"Le tour {self.name} est terminé.")

    def create_matches(self, players_list: List[Player], pairs_already_played: Set[Tuple[str, str]]) -> None:
        """
        Creates matches for the round, avoiding already played pairs.

        :param players_list: List of players.
        :type players_list: list
        :param pairs_already_played: Set of already played pairs.
        :type pairs_already_played: set
        :return: None
        :rtype: None
        """
        i = 0
        while i < len(players_list) - 1:
            player1 = players_list[i]
            player2 = None
            pair = None

            # Attempt to find a valid opponent for player1
            for j in range(i + 1, len(players_list)):
                potential_opponent = players_list[j]
                potential_pair = (player1.national_id, potential_opponent.national_id)

                if potential_pair not in pairs_already_played and (potential_pair[::-1] not in pairs_already_played):
                    player2 = potential_opponent
                    pair = potential_pair
                    # Swap players to maintain match order
                    players_list[i + 1], players_list[j] = players_list[j], players_list[i + 1]
                    break

            if player2 is None:
                print(f"Impossible de trouver un nouvel adversaire pour {player1.last_name}. Il sera exempté.")
                break

            # Add the match and update played pairs
            match = ([player1, 0.0], [player2, 0.0])
            self.matches.append(match)
            pairs_already_played.add(pair)
            i += 2

        # If there's an odd number of players, the last one is exempt
        if len(players_list) % 2 != 0:
            remaining_player = players_list[-1]
            print(f"{remaining_player.last_name} est exempté ce tour.")
            self.matches.append(([remaining_player, 0.0], [None, None]))

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the round to a dictionary.

        :return: Dictionary representation of the round
        :rtype: dict
        """
        matches_as_dict = []
        for match in self.matches:
            player1, score1 = match[0]
            player2, score2 = match[1]
            match_dict = {
                'player1': player1.to_dict() if player1 else None,
                'score1': score1,
                'player2': player2.to_dict() if player2 else None,
                'score2': score2
            }
            matches_as_dict.append(match_dict)

        return {
            'name': self.name,
            'number': self.number,  # Include round number
            'start_datetime': self.start_datetime.strftime('%d/%m/%Y %H:%M:%S'),
            'end_datetime': self.end_datetime.strftime('%d/%m/%Y %H:%M:%S') if self.end_datetime else None,
            'matches': matches_as_dict
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Round':
        """
        Creates a Round instance from a dictionary.

        :param data: Dictionary containing round data.
        :type data: dict
        :return: Round instance.
        :rtype: Round
        """
        round_instance = cls(name=data["name"], number=data["number"])
        round_instance.start_datetime = datetime.strptime(
            data["start_datetime"], '%d/%m/%Y %H:%M:%S')
        round_instance.end_datetime = datetime.strptime(
            data["end_datetime"], '%d/%m/%Y %H:%M:%S') if data["end_datetime"] else None
        for match_data in data["matches"]:
            player1 = Player.from_dict(match_data["player1"])
            score1 = match_data["score1"]
            player2 = Player.from_dict(match_data["player2"])
            score2 = match_data["score2"]
            round_instance.matches.append(
                ([player1, score1], [player2, score2]))
        return round_instance