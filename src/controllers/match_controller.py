from views.match_view import MatchView

class MatchController:
    """
    Manages the operations related to a match.

    :param match: A tuple containing information about the two players and their scores
    :type match: tuple
    :return: None
    :rtype: None
    """

    def __init__(self, match):
        self.match = match

    def play_match(self):
        player1_info, player2_info = self.match
        player1, score1 = player1_info
        player2, score2 = player2_info

        result = input(f"Qui a gagné ? (1 pour {player1.last_name}, 2 pour {player2.last_name}, N pour match nul) : ")
        if result == '1':
            player1.points += 1
            player1_info[1] = 1
            player2_info[1] = 0
        elif result == '2':
            player2.points += 1
            player1_info[1] = 0

            player2_info[1] = 1
        elif result.lower() == 'n':
            player1.points += 0.5
            player2.points += 0.5
            player1_info[1] = 0.5
            player2_info[1] = 0.5
        else:
            MatchView.display_message("Entrée invalide. Match nul par défaut.")
            player1.points += 0.5
            player2.points += 0.5
            player1_info[1] = 0.5
            player2_info[1] = 0.5

