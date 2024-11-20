from models.tournoi_model import Tournoi
from models.joueur_model import Joueur
from controllers.tour_controller import TourController
from views.tournoi_view import TournoiView
from controllers.joueur_controller import JoueurController

from datetime import datetime
from typing import List, Optional, Union


class TournoiController:
    def __init__(self):
        """Initialize the TournoiController with loaded tournaments and a JoueurController instance."""
        self.tournois: List[Tournoi] = Tournoi.charger_tournois()
        self.joueur_controller: JoueurController = JoueurController()

    def creer_tournoi(self) -> None:
        """Create a new tournament and add players to it."""
        # Create the tournament
        nom, lieu, nb_tours, description = TournoiView.demander_informations_tournoi()
        tournoi: Tournoi = Tournoi(nom, lieu, int(nb_tours), description)

        # Add players to the tournament
        print("\n--- Adding players to the tournament ---")

        joueurs_disponibles: List[Joueur] = self.joueur_controller.joueurs
        if not joueurs_disponibles:
            print("No players available for this tournament.")
            return

        # Display players with numbers for selection
        for index, joueur in enumerate(joueurs_disponibles, start=1):
            print(f"{index}. {joueur.nom} {joueur.prenom} (ID: {joueur.id_national})")

        # Loop to allow selection of multiple players
        joueurs_ajoutes: set = set()  # To avoid duplicates
        while True:
            choix: str = input("Enter the number(s) of the players to add (e.g., 1,3,5 or 'fin' to finish): ")
            if choix.lower() == 'fin':
                break

            try:
                # Split the string by commas and convert each part to an index
                indices: List[int] = [int(num.strip()) - 1 for num in choix.split(',')]
                for index in indices:
                    if 0 <= index < len(joueurs_disponibles):
                        joueur: Joueur = joueurs_disponibles[index]
                        if joueur not in joueurs_ajoutes:
                            tournoi.ajouter_joueur(joueur)
                            joueurs_ajoutes.add(joueur)
                            print(f"Player {joueur.nom} {joueur.prenom} added to the tournament.")
                        else:
                            print(f"Player {joueur.nom} {joueur.prenom} already added to the tournament.")
                    else:
                        print(f"The number {index + 1} is invalid. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

        # Finalize the creation of the tournament
        self.tournois.append(tournoi)
        Tournoi.sauvegarder_tournois(self.tournois)
        print("Tournament created successfully.")

    def demarrer_tournoi(self, tournoi: Tournoi) -> None:
        """Start the tournament and manage its rounds.

        :param tournoi: The tournament to start
        :type tournoi: Tournoi
        """
        tours_restants: int = tournoi.nb_tours - tournoi.tour_actuel
        for i in range(tournoi.tour_actuel, tours_restants):
            tour_controller: TourController = TourController(tournoi)
            tour_controller.demarrer_tour(i)
            # Increment the current round if necessary
            # tournoi.tour_actuel += 1  # Uncomment if the increment is not done elsewhere
            Tournoi.sauvegarder_tournois(self.tournois)
        # The tournament is finished
        tournoi.terminer()
        Tournoi.sauvegarder_tournois(self.tournois)
        classement: List[Joueur] = tournoi.get_classement()
        TournoiView.afficher_classement(classement)

    def lister_tournois(self) -> None:
        """List all tournaments."""
        self.tournois = Tournoi.charger_tournois()
        TournoiView.afficher_liste_tournois(self.tournois)

    def selectionner_tournoi(self) -> Optional[Tournoi]:
        """Select a tournament that has not yet ended.

        :return: The selected tournament or None if no tournament is selected
        :rtype: Optional[Tournoi]
        """
        # Filter tournaments to display only those that do not have an end date
        tournois_en_cours: List[Tournoi] = [tournoi for tournoi in self.tournois if not tournoi.date_fin]
        if not tournois_en_cours:
            print("No ongoing tournaments available.")
            return None

        print("\n--- List of available tournaments ---")
        for index, tournoi in enumerate(tournois_en_cours, start=1):
            # Convert to datetime if `date_debut` is a string
            date_debut: Union[datetime, str] = datetime.strptime(tournoi.date_debut, "%d/%m/%Y") if isinstance(tournoi.date_debut, str) else tournoi.date_debut
            date_fin: str = "Ongoing"  # Display for ongoing tournaments

            # Formatted display
            date_debut_str: str = date_debut.strftime("%d/%m/%Y") if date_debut else "Not defined"
            print(f"{index}. {tournoi.nom} started on {date_debut_str} (at {tournoi.lieu}) ")

        while True:
            choix: str = input("Enter the number of the tournament to select (or 'retour' to return to the main menu): ")
            if choix.lower() == 'retour':
                return None  # Allows returning to the main menu

            try:
                index: int = int(choix) - 1
                if 0 <= index < len(tournois_en_cours):
                    return tournois_en_cours[index]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def afficher_details_tournoi(self, tournoi: Tournoi) -> None:
        """Display the details of a tournament.

        :param tournoi: The tournament whose details are to be displayed
        :type tournoi: Tournoi
        """
        TournoiView.afficher_informations_tournoi(tournoi)
        TournoiView.afficher_classement(tournoi.get_classement())