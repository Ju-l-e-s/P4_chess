# controllers/round_controller.py
from datetime import datetime
from controllers.match_controller import MatchController
from models.round_model import Round
from models.tournament_model import Tournament
from views.round_view import RoundView

class RoundController:
    """
    Manages the operations related to rounds in a tournament.

    :param tournament: The tournament instance that this controller is managing rounds for.
    :type tournament: Tournament
    :return: None
    :rtype: None
    """


    def __init__(self, tournament: Tournament) -> None:
        self.tournament = tournament

    def start_round(self, round_number: int) -> None:
        RoundView.display_start_round(round_number)

        round_instance = Round(name=f"Round {round_number}", number=round_number)
        round_instance.create_matches(self.tournament.players, self.tournament.pairs_already_played)

        for match in round_instance.matches:
            match_controller = MatchController(match)
            match_controller.play_match()

        self.tournament.add_round(round_instance)
        round_instance.end_datetime = datetime.now()

        Tournament.save_tournaments([self.tournament])

        RoundView.display_end_round(round_number)