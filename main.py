from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController

def main() -> None:
    """
    Displays the main menu and handles navigation between submenus.

    :param None
    :type None
    :raises KeyboardInterrupt: If the user interrupts the script with Ctrl+C.
    :return: None
    :rtype: None
    """
    while True:
        print("\n--- Menu principal ---")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter")
        choice: str = input("Choisir une option: ")

        if choice == '1':
            player_submenu()
        elif choice == '2':
            tournament_submenu()
        elif choice == '3':
            report_submenu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Choix invalide, essayez autre chose.")

def player_submenu() -> None:
    """
    Displays the player submenu and handles options.

    :return: None
    :rtype: None
    """
    controller = PlayerController()
    while True:
        print("\n--- Player Menu ---")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour au menu principal")
        choice: str = input("Sélectionner une option: ")

        if choice == '1':
            controller.add_player()
        elif choice == '2':
            controller.list_players_alphabetically()
        elif choice == '3':
            break
        else:
            print("Choix invalide, essayez autre chose.")

def tournament_submenu() -> None:
    """
    Displays the tournament submenu and handles options.

    :return: None
    :rtype: None
    """
    controller = TournamentController()
    while True:
        print("\n--- Menu Tournoi ---")
        print("1. Creer un tournoi")
        print("2. Débuter un tournoi")
        print("3. Liste des tournois")
        print("4. Retour au menu principal")
        choice: str = input("Sélectionner une option: ")

        if choice == '1':
            controller.create_tournament()
        elif choice == '2':
            tournament = controller.select_tournament()
            if tournament:
                controller.start_tournament(tournament)
        elif choice == '3':
            controller.list_tournaments()
        elif choice == '4':
            break
        else:
            print("Choix invalide, essayez autre chose.")

def report_submenu() -> None:
    """
    Displays the reports submenu and handles options.

    :return: None
    :rtype: None
    """
    controller = ReportController()
    while True:
        print("\n--- Menu Rapports ---")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Afficher les détails du tournoi")
        print("4. Retour au menu principal")
        choice: str = input("Sélectionner une option: ")

        if choice == '1':
            controller.display_all_players()
        elif choice == '2':
            controller.display_all_tournaments()
        elif choice == '3':
            tournament = controller.tournament_controller.select_tournament()
            if tournament:
                controller.display_tournament_details(tournament)
        elif choice == '4':
            break
        else:
            print("Choix invalide, essayez autre chose.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrompu par l'utilisateur.")