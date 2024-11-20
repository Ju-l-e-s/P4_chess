# views/joueur_view.py

class JoueurView:
    def afficher_joueurs(joueurs: list) -> None:
        """
        Display the list of players with their details.

        :param joueurs: List of player objects to display
        :type joueurs: list
        :return: None
        :rtype: None
        """

    def demander_informations_joueur() -> tuple:
        """
        Prompt the user to enter player information.

        :return: A tuple containing the player's last name, first name, birth date, and national ID
        :rtype: tuple
        """
    @staticmethod
    def afficher_joueurs(joueurs):
        for joueur in joueurs:
            print(f"{joueur.nom} {joueur.prenom} (ID: {joueur.id_national}) - Points: {joueur.points}")

    @staticmethod
    def demander_informations_joueur():
        nom = input("Nom de famille : ")
        prenom = input("Prénom : ")
        date_naissance = input("Date de naissance (jj/mm/aaaa) : ")
        id_national = input("Identifiant national (ex: AB12345) : ")
        return nom, prenom, date_naissance, id_national
