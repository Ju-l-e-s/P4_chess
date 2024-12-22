
from models.player_model import Player
from views.player_view import PlayerView
from typing import List

class PlayerController:
    """
    Manages the operations related to players.

    :param players: The list of players managed by this controller, defaults to an empty list
    :type players: list, optional
    :return: None
    :rtype: None
    """
    def __init__(self) -> None:
        """
        Initializes the player controller by loading existing players.

        :return: None
        :rtype: None
        """
        self.players: List[Player] = Player.load_players()
    def add_player(self) -> None:
        """
        Adds a new player by requesting their information from the user.

        :return: None
        :rtype: None
        """
        while True:
            try:
                last_name, first_name, birth_date, national_id = PlayerView.request_player_info()
                player = Player(last_name, first_name, birth_date, national_id)
                self.players.append(player)
                Player.save_players(self.players)
                PlayerView.display_player_added_successfully()
                break
            except ValueError as e:
                PlayerView.display_error(e)

    def list_players(self) -> None:
        """
        Displays the list of players sorted by last name.

        :return: None
        :rtype: None
        """
        self.players = Player.load_players()
        self.players.sort(key=lambda p: p.last_name)
        PlayerView.display_players(self.players)

    def list_players_alphabetically(self) -> None:
        """
        Displays the list of players sorted alphabetically by last name and first name.

        :return: None
        :rtype: None
        """
        self.players = Player.load_players()
        self.players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(self.players)

        self.players: List[Player] = Player.load_players()
    def add_player(self) -> None:
        """
        Adds a new player by requesting their information from the user.

        :return: None
        :rtype: None
        """
        while True:
            try:
                last_name, first_name, birth_date, national_id = PlayerView.request_player_info()
                player = Player(last_name, first_name, birth_date, national_id)
                self.players.append(player)
                Player.save_players(self.players)
                PlayerView.display_player_added_successfully()
                break
            except ValueError as e:
                PlayerView.display_error(e)

    def list_players(self) -> None:
        """
        Displays the list of players sorted by last name.

        :return: None
        :rtype: None
        """
        self.players = Player.load_players()
        self.players.sort(key=lambda p: p.last_name)
        PlayerView.display_players(self.players)

    def list_players_alphabetically(self) -> None:
        """
        Displays the list of players sorted alphabetically by last name and first name.

        :return: None
        :rtype: None
        """
        self.players = Player.load_players()
        self.players.sort(key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(self.players)
