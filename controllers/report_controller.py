from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from models.player_model import Player
from models.tournament_model import Tournament
from typing import List

class ReportController:
    """
    Manages the generation of reports for the tournament.

    :param tournament: The tournament associated with this controller, defaults to None
    :type tournament: Tournament, optional
    :param players: The list of players in the tournament, defaults to an empty list
    :type players: list, optional
    :param rounds: The list of rounds in the tournament, defaults to an empty list
    :type rounds: list, optional
    :return: None
    :rtype: None
    """
    def __init__(self) -> None:
        """
        Initializes the report controller.

        :return: None
        :rtype: None
        """
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def display_all_players(self) -> None:
        """
        Displays the list of all players alphabetically.

        :return: None
        :rtype: None
        """
        players: List[Player] = self.player_controller.players
        players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(players)

    def display_all_tournaments(self) -> None:
        """
        Displays the list of all tournaments.

        :return: None
        :rtype: None
        """
        tournaments: List[Tournament] = self.tournament_controller.tournaments
        TournamentView.display_tournaments_list(tournaments)

    def display_tournament_details(self, tournament: Tournament) -> None:
        """
        Displays the details of a tournament, including players, rounds, and matches.

        :param tournament: The tournament whose details are to be displayed.
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        TournamentView.display_tournament_info(tournament)
        players = tournament.players
        players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(players)
        TournamentView.display_rounds_and_matches(tournament)
