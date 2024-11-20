from models.tournament_model import Tournament
from models.player_model import Player
from controllers.round_controller import RoundController
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController

from datetime import datetime
from typing import List, Optional, Union

class TournamentController:
    """
    Manages the operations related to tournaments.

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
        Initializes the tournament controller by loading existing tournaments.

        :return: None
        :rtype: None
        """
        self.tournaments: List[Tournament] = Tournament.load_tournaments()
        self.player_controller: PlayerController = PlayerController()

    def create_tournament(self) -> None:
        """
        Creates a new tournament by requesting necessary information.

        :return: None
        :rtype: None
        """
        # Request tournament information
        name, location, number_of_rounds, description = TournamentView.request_tournament_info()
        tournament: Tournament = Tournament(name, location, int(number_of_rounds), description)

        # Add players to the tournament
        TournamentView.display_message("\n--- Adding players to the tournament ---")

        available_players: List[Player] = self.player_controller.players
        if not available_players:
            TournamentView.display_message("No players available for this tournament.")
            return

        # Display players with numbers for selection
        TournamentView.display_players_list_with_indices(available_players)

        # Loop to allow selection of multiple players
        added_players: set = set()  # To avoid duplicates
        while True:
            choice: str = input("Enter the numbers of the players to add (e.g., 1,3,5 or 'done' to finish): ")
            if choice.lower() == 'done':
                break

            try:
                # Split the string by commas and convert each part to an index
                indices: List[int] = [int(num.strip()) - 1 for num in choice.split(',')]
                for index in indices:
                    if 0 <= index < len(available_players):
                        player: Player = available_players[index]
                        if player not in added_players:
                            tournament.add_player(player)
                            added_players.add(player)
                            TournamentView.display_message(f"Player {player.last_name} {player.first_name} added to the tournament.")
                        else:
                            TournamentView.display_message(f"Player {player.last_name} {player.first_name} already added to the tournament.")
                    else:
                        TournamentView.display_message(f"The number {index + 1} is invalid. Please enter a valid number.")
            except ValueError:
                TournamentView.display_message("Invalid input. Please enter numbers separated by commas.")

        # Finalize the creation of the tournament
        self.tournaments.append(tournament)
        Tournament.save_tournaments(self.tournaments)
        TournamentView.display_message("Tournament created successfully.")

    def start_tournament(self, tournament: Tournament) -> None:
        """
        Starts the tournament and manages its rounds.

        :param tournament: The tournament to start
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        # Record the start date if the tournament begins
        if tournament.current_round == 0 and not tournament.start_date:
            tournament.start_date = datetime.now().strftime('%d/%m/%Y')

        for i in range(tournament.current_round, tournament.number_of_rounds):
            round_controller: RoundController = RoundController(tournament)
            round_controller.start_round(i + 1)
            Tournament.save_tournaments(self.tournaments)
        # The tournament is finished
        tournament.end()
        Tournament.save_tournaments(self.tournaments)
        ranking: List[Player] = tournament.get_ranking()
        TournamentView.display_ranking(ranking)

    def list_tournaments(self) -> None:
        """
        Displays the list of all tournaments.

        :return: None
        :rtype: None
        """
        self.tournaments = Tournament.load_tournaments()
        TournamentView.display_tournaments_list(self.tournaments)

    def select_tournament(self) -> Optional[Tournament]:
        """
        Allows selecting a tournament that is not yet finished.

        :return: The selected tournament or None if no tournament is selected
        :rtype: Optional[Tournament]
        """
        # Filter tournaments to display only those that do not have an end date
        ongoing_tournaments: List[Tournament] = [tournament for tournament in self.tournaments if not tournament.end_date]
        if not ongoing_tournaments:
            TournamentView.display_message("No ongoing tournaments available.")
            return None

        TournamentView.display_ongoing_tournaments(ongoing_tournaments)

        while True:
            choice: str = input("Enter the number of the tournament to select (or 'back' to return to the main menu): ")
            if choice.lower() == 'back':
                return None

            try:
                index: int = int(choice) - 1
                if 0 <= index < len(ongoing_tournaments):
                    return ongoing_tournaments[index]
                else:
                    TournamentView.display_message("Invalid choice. Please enter a valid number.")
            except ValueError:
                TournamentView.display_message("Invalid input. Please enter a number.")

    def display_tournament_details(self, tournament: Tournament) -> None:
        """
        Displays the details of a tournament.

        :param tournament: The tournament whose details are to be displayed
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        TournamentView.display_tournament_info(tournament)
        TournamentView.display_ranking(tournament.get_ranking())
        TournamentView.display_rounds_and_matches(tournament)
