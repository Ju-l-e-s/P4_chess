from models.player_model import Player


class MatchView:
    """
    Provides methods to display match information and interact with the user.

    :param None
    :type None
    :return: None
    :rtype: None
    """

    def display_match(match):
        """
        Displays the match information.

        :param match: The match to display
        :type match: Tuple[List[Any], List[Any]]
        :return: None
        :rtype: None
        """
        player1_info, player2_info = match
        player1, score1 = player1_info
        player2, score2 = player2_info
        print(
            f"{player1.last_name} {player1.first_name} ({score1}) vs {player2.last_name} {player2.first_name} ({score2})")

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
        result = input(
            "Qui a gagné ? (1 pour joueur 1, 2 pour joueur 2, N pour match nul) : ")
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
