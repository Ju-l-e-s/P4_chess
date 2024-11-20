from typing import List, Tuple, Optional
from models.joueur_model import Joueur
from models.tournoi_model import Tournoi

class TournoiView:
    @staticmethod
    def afficher_informations_tournoi(tournoi: Tournoi) -> None:
        """
        Display tournament information.

        :param tournoi: The tournament object containing information to display
        :type tournoi: Tournoi
        :return: None
        :rtype: None
        """
        print(f"Tournoi : {tournoi.nom}")
        print(f"Lieu : {tournoi.lieu}")
        print(f"Date de début : {tournoi.date_debut}")
        if tournoi.date_fin:
            print(f"Date de fin : {tournoi.date_fin}")
        else:
            print("Date de fin : En cours")
        print(f"Nombre de tours : {tournoi.nb_tours}")
        print(f"Description : {tournoi.description}")
        
    @staticmethod
    def afficher_classement(joueurs: List[Joueur]) -> None:
        """
        Display the ranking of players.

        :param joueurs: List of players to display in the ranking
        :type joueurs: List[Joueur]
        :return: None
        :rtype: None
        """
        print("\n--- Classement des Joueurs ---")
        for i, joueur in enumerate(joueurs, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} - {joueur.points} points")

    @staticmethod
    def demander_informations_tournoi() -> Tuple[str, str, str, str]:
        """
        Prompt the user for tournament information.

        :return: A tuple containing the tournament name, location, number of rounds, and description
        :rtype: Tuple[str, str, str, str]
        """
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        nb_tours = input("Nombre de tours (par défaut 4) : ") or '4'
        description = input("Description : ")
        return nom, lieu, nb_tours, description

    @staticmethod
    def afficher_liste_tournois(tournois: List['Tournoi']) -> None:
        """
        Display a list of tournaments.

        :param tournois: List of tournaments to display
        :type tournois: List[Tournoi]
        :return: None
        :rtype: None
        """
        for tournoi in tournois:
            print(f"- {tournoi.nom} à {tournoi.lieu} du {tournoi.date_debut} au {tournoi.date_fin}")
