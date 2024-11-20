from models.round_model import Round
from controllers.match_controller import MatchController
from models.tournament_model import Tournament
from models.player_model import Player

import random
from typing import List

class RoundController:
    """
    Manages the operations related to tournament rounds.

    :param tournament: The tournament instance to manage.
    :type tournament: Tournament
    :param players: The list of players in the tournament, defaults to an empty list
    :type players: list, optional
    :param rounds: The list of rounds in the tournament, defaults to an empty list
    :type rounds: list, optional
    :return: None
    :rtype: None
    """

    def __init__(self, tournament: Tournament) -> None:
        """
        Initializes the RoundController with a tournament.

        :param tournament: The tournament instance to manage.
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        self.tournament = tournament

    def start_round(self, round_number: int) -> None:
        """
        Starts a new round in the tournament.

        :param round_number: The number of the round to start.
        :type round_number: int
        :return: None
        :rtype: None
        """
        round_instance = Round(f"Round {round_number}")
        if self.tournament.current_round == 0:
            # First round: shuffle players
            players: List[Player] = self.tournament.players.copy()
            random.shuffle(players)
        else:
            # Subsequent rounds: sort by points
            players = sorted(self.tournament.players, key=lambda p: (-p.points, p.last_name))
        # Create matches
        round_instance.create_matches(players, self.tournament.pairs_already_played)
        self.tournament.add_round(round_instance)
        # Manage matches
        for match in round_instance.matches:
            match_controller = MatchController(match)
            match_controller.play_match()
            # Record played pairs
            pair = (match.player1.national_id, match.player2.national_id)
            self.tournament.pairs_already_played.add(pair)
        round_instance.end(self.tournament)
