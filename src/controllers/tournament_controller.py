from models.tournament_model import Tournament
from models.player_model import Player
from controllers.round_controller import RoundController
from utils.clear import clear_terminal
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController

from datetime import datetime
from typing import List, Optional


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
        tournament: Tournament = Tournament(
            name, location, int(number_of_rounds), description)

        available_players: List[Player] = self.player_controller.players
        # Add players to the tournament
        TournamentView.display_message(
            "\n--- Ajout des joueurs au tournoi ---")

        available_players: List[Player] = self.player_controller.players
        if not available_players:
            TournamentView.display_message(
                "Aucun joueur disponible pour ce tournoi.")
            return

        # Display players with numbers for selection
        TournamentView.display_players_list_with_indices(available_players)

        # Loop to allow selection of multiple players
        added_players: set = set()  # To avoid duplicates
        while True:
            choice: str = input(
                "Entrez les numéros des joueurs à ajouter (par exemple, 1,3,5 ou 't' pour terminer) : ")
            if choice.lower() == 't':
                break

            try:
                # Split the string by commas and convert each part to an index
                indices: List[int] = [
                    int(num.strip()) - 1 for num in choice.split(',')]
                for index in indices:
                    if 0 <= index < len(available_players):
                        player: Player = available_players[index]
                        if player not in added_players:
                            tournament.add_player(player)
                            added_players.add(player)
                            TournamentView.display_message(f"Joueur {player.last_name} {player.first_name} ajouté au tournoi.")
                        else:
                            TournamentView.display_message(f"Joueur {player.last_name} {player.first_name} déjà ajouté au tournoi.")
                    else:
                        TournamentView.display_message(
                            f"Le numéro {index + 1} est invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                TournamentView.display_message(
                    "Entrée invalide. Veuillez entrer des numéros séparés par des virgules.")

        # Finalize the creation of the tournament
        self.tournaments.append(tournament)
        Tournament.save_tournaments(self.tournaments)
        TournamentView.display_message("Tournoi créé avec succès.")

    def start_tournament(self, tournament: Tournament) -> None:
        """
        Starts the tournament and manages its rounds.

        :param tournament: The tournament to start
        :type tournament: Tournament
        :return: None
        :rtype: None
        """
        if tournament.current_round == 0 and not tournament.start_date:
            tournament.start_date = datetime.now().strftime('%d/%m/%Y')

        for i in range(tournament.current_round, tournament.number_of_rounds):
            round_controller = RoundController(tournament)
            round_controller.start_round(i + 1)
            Tournament.save_tournaments(self.tournaments)

        tournament.end()
        Tournament.save_tournaments(self.tournaments)
        print("\n--- Tournament Completed ---")

        # Appel correct de la méthode d'affichage
        TournamentView.display_tournament_summary_from_json(tournament.to_dict())

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
        ongoing_tournaments: List[Tournament] = [
            tournament for tournament in self.tournaments if not tournament.end_date]
        if not ongoing_tournaments:
            clear_terminal()
            TournamentView.display_message(
                "Pas de tournoi dans la base de donnée ne correspondant à votre recherche.")
            return None

        TournamentView.display_ongoing_tournaments(ongoing_tournaments)

        while True:
            choice: str = input(
                "Entrez le numéro du tournoi à sélectionner (ou 'retour' pour revenir au menu principal) : ")
            if choice.lower() == 'retour':
                return None

            try:
                index: int = int(choice) - 1
                if 0 <= index < len(ongoing_tournaments):
                    return ongoing_tournaments[index]
                else:
                    TournamentView.display_message(
                        "Choix invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                TournamentView.display_message(
                    "Entrée invalide. Veuillez entrer un numéro.")

    def load_and_display_tournament_summary(tournament_name: str) -> None:
        """
        Loads a tournament from the JSON file and displays its summary.

        :param tournament_name: The name of the tournament to load.
        :type tournament_name: str
        :return: None
        :rtype: None
        """
        tournaments = Tournament.load_tournaments()
        for tournament_data in tournaments:
            if tournament_data["name"] == tournament_name:
                TournamentView.display_tournament_summary_from_json(
                    tournament_data)
                return
        print("Tournoi non trouvé.")
