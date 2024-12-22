from models.tournament_model import Tournament
from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from utils.clear import clear_terminal


class MenuController:
    def __init__(self):
        """Initialize MenuController with MenuView instance."""
        self.view = MenuView()
        self.report_controller = ReportController()

    def tournament_submenu(self) -> None:
        """
        Manages the tournament submenu and its options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        controller = TournamentController()

        while True:
            self.view.display_tournament_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                clear_terminal()
                controller.create_tournament()
            elif choice == '2':
                clear_terminal()
                tournament = controller.select_tournament()
                if tournament:
                    controller.start_tournament(tournament)
            elif choice == '3':
                clear_terminal()
                # Demander de sélectionner un tournoi
                tournament = controller.select_tournament()
                if tournament:
                    self.report_controller.display_tournament_details(tournament)
                else:
                    print("Aucun tournoi n'est pret à démarrer.")
            elif choice == '4':
                clear_terminal()
                break
            else:
                clear_terminal()
                self.view.display_invalid_choice()

    def player_submenu(self) -> None:
        """
        Manages the player submenu and its options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        controller = PlayerController()

        while True:
            self.view.display_player_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                clear_terminal()
                controller.add_player()
            elif choice == '2':
                clear_terminal()
                controller.list_players_alphabetically()
            elif choice == '3':
                clear_terminal()
                break
            else:
                clear_terminal()
                self.view.display_invalid_choice()

    def run(self) -> None:
        """
        Manages the main menu and navigation between submenus.

        :param None
        :type None
        :raises KeyboardInterrupt: If the user interrupts the script with Ctrl+C
        :return: None
        :rtype: None
        """
        clear_terminal()

        while True:
            self.view.display_main_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                self.player_submenu()
            elif choice == "2":
                clear_terminal()
                self.tournament_submenu()
            elif choice == "3":
                clear_terminal()
                self.report_submenu()
            elif choice == "4":
                self.view.display_goodbye()
                break
            else:
                self.view.display_invalid_choice()

    def report_submenu(self) -> None:
        """
        Manages the report submenu and its options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        controller = ReportController()

        while True:
            self.view.display_report_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                clear_terminal()
                controller.display_all_players()
            elif choice == '2':
                clear_terminal()
                controller.display_all_tournaments()
            elif choice == '3':
                clear_terminal()
                # Charger les tournois et permettre la sélection
                tournaments = Tournament.load_tournaments()
                if tournaments:
                    print("Tournois disponibles :")
                    for index, tournament in enumerate(tournaments, start=1):
                        print(f"{index}. {tournament.name} à {tournament.location}")

                    try:
                        choice = int(input("Sélectionnez un tournoi par son numéro (ou 0 pour annuler) : "))
                        if choice == 0:
                            print("Retour au menu principal.")
                            return
                        elif 1 <= choice <= len(tournaments):
                            selected_tournament = tournaments[choice - 1]
                            controller.display_tournament_details(selected_tournament)
                        else:
                            print("Choix invalide. Retour au menu principal.")
                    except ValueError:
                        print("Entrée invalide. Retour au menu principal.")
                else:
                    print("Aucun tournoi disponible.")
            elif choice == '4':
                clear_terminal()
                break
            else:
                clear_terminal()
                self.view.display_invalid_choice()