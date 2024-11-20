from typing import List

class PlayerView:
    """
    Provides methods to display player information and interact with the user.

    :param None
    :type None
    :return: None
    :rtype: None
    """
    @staticmethod
    def display_players(players: List) -> None:
        """
        Displays the list of players with their details.

        :param players: List of players to display
        :type players: list
        :return: None
        :rtype: None
        """
        print("\n--- Liste des Joueurs ---")
        for player in players:
            print(f"{player.last_name} {player.first_name} (ID: {player.national_id})")

    @staticmethod
    def request_player_info() -> tuple:
        """
        Prompts the user to enter player information.

        :return: Tuple containing the player's last name, first name, birth date, and national ID
        :rtype: tuple
        """
        last_name: str = input("Nom de famille: ")
        first_name: str = input("Prénom: ")
        birth_date: str = input("Date de naissance (jj/mm/aaaa): ")
        national_id: str = input("ID National (ex: AB12345): ")
        return last_name, first_name, birth_date, national_id

    @staticmethod
    def display_player_added_successfully() -> None:
        """
        Displays a message indicating that the player was added successfully.

        :return: None
        :rtype: None
        """
        print("Joueur ajouté avec succès.")

    @staticmethod
    def display_error(error: Exception) -> None:
        """
        Displays an error message.

        :param error: The exception to display
        :type error: Exception
        :return: None
        :rtype: None
        """
        print(f"Erreur: {error}")
        print("Veuillez réessayer.")
