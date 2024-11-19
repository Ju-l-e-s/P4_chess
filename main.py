import sys
from controllers.tournoi_controller import TournoiController
from controllers.joueur_controller import JoueurController

def main():
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
            # Code pour ajouter un joueur, avec option pour revenir en arrière
            tournoi_controller.joueur_controller.ajouter_joueur()
        elif choix == '2':
            tournoi_controller.joueur_controller.lister_joueurs()
        elif choix == '3':
            tournoi_controller.creer_tournoi()
        elif choix == '4':
            tournoi_controller.lister_tournois()
        elif choix == '5':
            tournoi = tournoi_controller.selectionner_tournoi()
            if tournoi:
                tournoi_controller.demarrer_tournoi(tournoi)
        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrompu par l'utilisateur.")
        sys.exit(0)
()