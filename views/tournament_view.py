from typing import List, Tuple
from models.player_model import Player
from models.tournament_model import Tournament
from models.round_model import Round
from models.match_model import Match

class TournamentView:
    """
    Provides methods to display tournament information and interact with the user.

    :param None
    :type None
    :return: None
    :rtype: None
    """
    @staticmethod
    def display_tournament_info(tournament: Tournament) -> None:
        """
        Displays tournament information.

        :param tournament: The tournament to display
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        print(f"\n--- Tournoi: {tournament.name} ---")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date or 'Non commencé'}")
        print(f"Date de fin: {tournament.end_date or 'En cours'}")
        print(f"Nombre de tours: {tournament.number_of_rounds}")
        print(f"Description: {tournament.description}")

    @staticmethod
    def display_ranking(players: List[Player]) -> None:
        """
        Displays the ranking of players.

        :param players: List of players to display
        :type players: List[Player]
        :return: None
        :rtype: None
        """
        print("\n--- Player Rankings ---")
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player.last_name} {player.first_name} - {player.points} points")

    @staticmethod
    def request_tournament_info() -> Tuple[str, str, str, str]:
        """
        Prompts the user to enter tournament information.

        :return: Tuple containing the name, location, number of rounds, and description of the tournament
        :rtype: tuple
        """
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        number_of_rounds = input("Nombre de tours (par défaut 4): ") or '4'
        description = input("Description: ")
        return name, location, number_of_rounds, description

    @staticmethod
    def display_tournaments_list(tournaments: List[Tournament]) -> None:
        """
        Displays the list of tournaments.

        :param tournaments: List of tournaments to display
        :type tournaments: List[Tournament]
        :return: None
        :rtype: None
        """
        print("\n--- Liste des Tournois ---")
        for tournament in tournaments:
            print(f"- {tournament.name} in {tournament.location} from {tournament.start_date or 'Not started'} to {tournament.end_date or 'Ongoing'}")

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

    @staticmethod
    def display_players_list_with_indices(players: List[Player]) -> None:
        """
        Displays the list of players with indices for selection.

        :param players: List of players to display
        :type players: List[Player]
        :return: None
        :rtype: None
        """
        for index, player in enumerate(players, start=1):
            print(f"{index}. {player.last_name} {player.first_name} (ID: {player.national_id})")

    @staticmethod
    def display_ongoing_tournaments(tournaments: List[Tournament]) -> None:
        """
        Displays the list of ongoing tournaments.

        :param tournaments: List of ongoing tournaments
        :type tournaments: List[Tournament]
        :return: None
        :rtype: None
        """
        print("\n--- Tournois en cours ---")
        for index, tournament in enumerate(tournaments, start=1):
            start_date = tournament.start_date or "Non commencé"
            print(f"{index}. {tournament.name} commencé le {start_date} (à {tournament.location})")

    @staticmethod
    def display_rounds_and_matches(tournament: Tournament) -> None:
        """
        Displays all rounds of the tournament and all matches of each round.

        :param tournament: The tournament whose rounds and matches are to be displayed
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        print("\n--- Tours et Matchs du Tournoi ---")
        for round_instance in tournament.rounds:
            round_instance.display_info()
            for match in round_instance.matches:
                print(f"  {match.player1} vs {match.player2} - Score: {match.score_player1}-{match.score_player2}")
