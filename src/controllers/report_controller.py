# controllers/report_controller.py
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from models.player_model import Player
from models.tournament_model import Tournament
from typing import List

class ReportController:
    """
    Manages the operations related to reports, including displaying players and tournaments.

    :param player_controller: The controller managing player-related operations
    :type player_controller: PlayerController
    :param tournament_controller: The controller managing tournament-related operations
    :type tournament_controller: TournamentController
    :return: None
    :rtype: None
    """
    def __init__(self) -> None:
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def display_all_players(self) -> None:
        players: List[Player] = self.player_controller.players
        players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(players)

    def display_all_tournaments(self) -> None:
        tournaments: List[Tournament] = self.tournament_controller.tournaments
        TournamentView.display_tournaments_list(tournaments)

    def display_tournament_details(self, tournament: Tournament) -> None:
        TournamentView.display_tournament_info(tournament)
        players = tournament.players
        players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(players)
        TournamentView.display_rounds_and_matches_from_json(tournament.to_dict())
