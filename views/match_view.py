from models.match_model import Match


class MatchView:
    @staticmethod
    def afficher_match(match: Match) -> None:
        """
        Display the match information.

        :param match: The match object containing player information
        :type match: Match
        :return: None
        :rtype: None
        """
        print(f"{match.joueur1} vs {match.joueur2}")

    @staticmethod
    def demander_resultat_match(joueur1: str, joueur2: str) -> str:
        """
        Ask for the result of the match between two players.

        :param joueur1: Name of player 1
        :type joueur1: str
        :param joueur2: Name of player 2
        :type joueur2: str
        :return: The result of the match (1 pour le joeur 1, 2 pour le joueur 2, N pour match nul)
        :rtype: str
        """
        print(f"Match entre {joueur1} et {joueur2}")
        resultat = input(
            "Qui a gagné? (1 pour le joeur 1, 2 pour le joueur 2, N pour match nul): ")
        return resultat
