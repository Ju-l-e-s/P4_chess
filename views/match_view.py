from models.match_model import Match
from models.player_model import Player

class MatchView:
    """
    Provides methods to display match information and interact with the user.

    :param None
    :type None
    :return: None
    :rtype: None
    """
    @staticmethod
    def display_match(match: Match) -> None:
        """
        Displays match information.

        :param match: The match to display
        :type match: Match
        :return: None
        :rtype: None
        """
        print(f"{match.player1} vs {match.player2}")

    @staticmethod
    def request_match_result(player1: Player, player2: Player) -> str:
        """
        Requests the result of the match between two players.

        :param player1: First player
        :type player1: Player
        :param player2: Second player
        :type player2: Player
        :return: The result of the match ('1', '2', or 'N')
        :rtype: str
        """
        print(f"Match entre {player1} et {player2}")
        result = input("Qui a gagné ? (1 pour joueur 1, 2 pour joueur 2, N pour match nul) : ")
        return result

    @staticmethod
    def display_message(message: str) -> None:
        """
        Displays a message to the user.

        :param message: The message to display
        :type message: str
        :return: None
        :rtype: None
        """
        print(message)
