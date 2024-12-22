class MenuView:
    @staticmethod
    def display_main_menu() -> None:
        """
        Displays the main menu options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("\n--- Menu principal ---")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter")

    @staticmethod
    def display_player_menu() -> None:
        """
        Displays the player menu options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("\n--- Menu joueurs ---")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour au menu principal")

    @staticmethod
    def display_tournament_menu() -> None:
        """
        Displays the tournament menu options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("\n--- Menu Tournoi ---")
        print("1. Créer un tournoi")
        print("2. Débuter un tournoi")
        print("3. Liste des tournois")
        print("4. Retour au menu principal")

    @staticmethod
    def display_report_menu() -> None:
        """
        Displays the report menu options.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("\n--- Menu Rapports ---")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Afficher les détails d'un tournoi")
        print("4. Retour au menu principal")

    @staticmethod
    def display_invalid_choice() -> None:
        """
        Displays the error message for an invalid choice.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("Choix invalide, essayez autre chose.")

    @staticmethod
    def display_goodbye() -> None:
        """
        Displays the goodbye message.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("Goodbye!")

    @staticmethod
    def display_interrupt() -> None:
        """
        Displays the script interruption message.

        :param None
        :type None
        :return: None
        :rtype: None
        """
        print("\nScript interrompu par l'utilisateur.")

    @staticmethod
    def get_user_choice() -> str:
        """
        Retrieves the user's choice.

        :param None
        :type None
        :return: The user's choice
        :rtype: str
        """
        return input("Sélectionner une option: ")
