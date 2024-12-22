from typing import List, Tuple, Dict
from models.player_model import Player
from models.tournament_model import Tournament

from utils.clear import clear_terminal


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

        print("\n--- Classement des joueurs ---")
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
            if not tournament.end_date:
                print(f"- {tournament.name} à {tournament.location}")
            else:
                print(f"- {tournament.name} à {tournament.location} du {tournament.start_date} au {tournament.end_date or 'En cours'}")

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
            start_date = tournament.start_date
            if not tournament.end_date:
                print(f"{index}. {tournament.name}")
            else:
                print(f"{index}. {tournament.name} commencé le {start_date} (à {tournament.location})")

    @staticmethod
    def display_rounds_and_matches_from_json(tournament_data: Dict) -> None:
        """
        Displays all rounds and their matches from the tournament JSON data.

        :param tournament_data: The tournament data loaded from JSON.
        :type tournament_data: dict
        :return: None
        :rtype: None
        """
        rounds = tournament_data.get("rounds", [])
        if not rounds:
            print("Aucun tour enregistré pour ce tournoi.")
            return

        print("\n--- Résultats des Tours ---")
        for round_data in rounds:
            round_name = round_data.get("name", "Nom inconnu")
            round_number = round_data.get("number", "Non défini")
            start_datetime = round_data.get("start_datetime", "Non défini")
            end_datetime = round_data.get("end_datetime", "Non défini")
            matches = round_data.get("matches", [])

            print(f"\nTour {round_number if round_number != 'Non défini' else round_name}")
            print(f"Début : {start_datetime}")
            print(f"Fin : {end_datetime}")

            for match_data in matches:
                player1 = match_data["player1"]
                player2 = match_data["player2"]
                score1 = match_data["score1"]
                score2 = match_data["score2"]

                if not player2:
                    print(f"  {player1['last_name']} {player1['first_name']} est exempt ce tour.")
                else:
                    print(
                        f"  {player1['last_name']} {player1['first_name']} ({score1}) vs "
                        f"{player2['last_name']} {player2['first_name']} ({score2})"
                    )

    @staticmethod
    def display_tournament_summary_from_json(tournament_data: Dict) -> None:
        """
        Displays a complete summary of the tournament, including rounds, matches, and player rankings.

        :param tournament_data: The tournament data loaded from JSON.
        :type tournament_data: dict
        :return: None
        :rtype: None
        """
        clear_terminal()
        print("\n--- Résumé du Tournoi ---")
        print(f"Tournoi : {tournament_data['name']}")
        print(f"Lieu : {tournament_data['location']}")
        print(f"Date de début : {tournament_data.get('start_date', 'Non commencé')}")
        print(f"Date de fin : {tournament_data.get('end_date', 'En cours')}")
        print(f"Nombre de tours : {tournament_data['number_of_rounds']}")
        print(f"Description : {tournament_data['description']}\n")

        # Display rounds and matches
        TournamentView.display_rounds_and_matches_from_json(tournament_data)

        # Final rankings
        print("\n--- Classement Final ---")
        players = tournament_data.get("players", [])
        sorted_players = sorted(players, key=lambda p: p["points"], reverse=True)
        for rank, player in enumerate(sorted_players, start=1):
            print(f"{rank}. {player['last_name']} {player['first_name']} - {player['points']} points")
