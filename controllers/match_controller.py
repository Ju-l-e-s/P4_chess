from models.match_model import Match
from views.match_view import MatchView

class MatchController:
    """
    Manages the operations related to matches.

    :param match: The match associated with this controller
    :type match: Match
    :return: None
    :rtype: None
    """
    def __init__(self, match: Match) -> None:
        """
        Initializes the MatchController.

        :param match: The match associated with this controller.
        :type match: Match
        :return: None
        :rtype: None
        """
        self.match = match

    def play_match(self) -> None:
        """
        Plays the match by displaying it and requesting the result.

        :return: None
        :rtype: None
        """
        # Display the match
        MatchView.display_match(self.match)
        # Request the result
        result = MatchView.request_match_result(self.match.player1, self.match.player2)
        self.record_result(result)

    def record_result(self, result: str) -> None:
        """
        Records the match result and updates the players' scores.

        :param result: The result of the match ('1' for player 1 win, '2' for player 2 win, 'N' for draw).
        :type result: str
        :return: None
        :rtype: None
        """
        if result == "1":
            self.match.score_player1 = 1
            self.match.score_player2 = 0
        elif result == "2":
            self.match.score_player1 = 0
            self.match.score_player2 = 1
        elif result.upper() == "N":
            self.match.score_player1 = 0.5
            self.match.score_player2 = 0.5
        else:
            MatchView.display_message("Invalid input. Please try again.")
            return self.play_match()
        # Update players' points
        self.match.player1.update_points(self.match.score_player1)
        self.match.player2.update_points(self.match.score_player2)
