import sys
from controllers.tournoi_controller import TournoiController
from controllers.joueur_controller import JoueurController

def main() -> None:
    """
    Main function to run the tournament management system.

    :raises KeyboardInterrupt: If the user interrupts the script with Ctrl+C.
    """
    tournoi_controller = TournoiController()
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("3. Créer un tournoi")
        print("4. Lister les tournois")
        print("5. Démarrer un tournoi")
        print("6. Quitter")
        choix = input("Votre choix : ")

        if choix.lower() == 'retour':
            continue  # L'utilisateur est déjà au menu principal, donc continue

        if choix == '1':
            """
            Add a player to the tournament.

            :return: None
            """
            tournoi_controller.joueur_controller.ajouter_joueur()
        elif choix == '2':
            """
            List all players in the tournament.

            :return: None
            """
            tournoi_controller.joueur_controller.lister_joueurs()
        elif choix == '3':
            """
            Create a new tournament.

            :return: None
            """
            tournoi_controller.creer_tournoi()
        elif choix == '4':
            """
            List all tournaments.

            :return: None
            """
            tournoi_controller.lister_tournois()
        elif choix == '5':
            """
            Start a selected tournament.

            :return: None
            """
            tournoi = tournoi_controller.selectionner_tournoi()
            if tournoi:
                tournoi_controller.demarrer_tournoi(tournoi)
        elif choix == '6':
            """
            Exit the program.

            :return: None
            """
            print("Au revoir !")
            break
        else:
            """
            Handle invalid menu choices.

            :return: None
            """
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrompu par l'utilisateur.")
        sys.exit(0)