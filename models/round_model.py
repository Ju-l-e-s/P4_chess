from datetime import datetime
from models.match_model import Match
from models.player_model import Player
from typing import List, Set, Tuple, Dict, Any, Optional

class Round:
    """
    Represents a round in the tournament.

    :param name: The name of the round
    :type name: str
    :param matches: The list of matches in the round, defaults to an empty list
    :type matches: list, optional
    :return: None
    :rtype: None
    """
    def __init__(self, name: str) -> None:
        """
        Initializes a Round instance.

        :param name: The name of the round.
        :type name: str
        :return: None
        :rtype: None
        """
        self.name: str = name
        self.start_datetime: datetime = datetime.now()
        self.end_datetime: Optional[datetime] = None
        self.matches: List[Match] = []

    def display_info(self) -> None:
        """
        Displays the round's information.

        :return: None
        :rtype: None
        """
        start_str = self.start_datetime.strftime("%d/%m/%Y %H:%M")
        end_str = self.end_datetime.strftime("%d/%m/%Y %H:%M") if self.end_datetime else "Ongoing"
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
        # Record match results
        for match in self.matches:
            match.record_result()
        # Check if the tournament is finished
        if tournament.current_round >= tournament.number_of_rounds:
            tournament.end()

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
            player2 = players_list[i + 1]

            # Check if the pair has already played together
            pair = (player1.national_id, player2.national_id)
            if pair in pairs_already_played or (pair[::-1] in pairs_already_played):
                # Find another opponent
                j = i + 2
                while j < len(players_list):
                    player2 = players_list[j]
                    new_pair = (player1.national_id, player2.national_id)
                    if new_pair not in pairs_already_played and (new_pair[::-1] not in pairs_already_played):
                        # Swap players to avoid the already played pair
                        players_list[i + 1], players_list[j] = players_list[j], players_list[i + 1]
                        break
                    j += 1
                else:
                    print(f"Impossible de trouver un nouvel adversaire pour {player1.last_name}")
            # Create the match
            match = Match(player1, player2)
            self.matches.append(match)
            # Add the pair to already played pairs
            pairs_already_played.add(pair)
            i += 2

        # Handle the case of a player without an opponent (odd number of players)
        if len(players_list) % 2 != 0:
            remaining_player = players_list[-1]
            print(f"{remaining_player.last_name} n'a pas d'adversaire ce tour (exempt).")

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the instance to a dictionary for JSON saving.

        :return: Dictionary representation of the instance.
        :rtype: dict
        """
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.strftime('%d/%m/%Y %H:%M:%S'),
            "end_datetime": self.end_datetime.strftime('%d/%m/%Y %H:%M:%S') if self.end_datetime else None,
            "matches": [match.to_dict() for match in self.matches]
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
        round_instance = cls(name=data["name"])
        round_instance.start_datetime = datetime.strptime(data["start_datetime"], '%d/%m/%Y %H:%M:%S')
        round_instance.end_datetime = datetime.strptime(data["end_datetime"], '%d/%m/%Y %H:%M:%S') if data["end_datetime"] else None
        round_instance.matches = [Match.from_dict(match_data) for match_data in data["matches"]]
        return round_instance
