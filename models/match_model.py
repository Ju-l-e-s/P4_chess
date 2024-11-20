from models.player_model import Player
from typing import Dict, Any

class Match:
    """
    Represents a match between two players.

    :param player1: The first player
    :type player1: Player
    :param player2: The second player
    :type player2: Player
    :return: None
    :rtype: None
    """
    def __init__(self, player1: Player, player2: Player) -> None:
        """
        Initializes a match with two players.

        :param player1: The first player
        :type player1: Player
        :param player2: The second player
        :type player2: Player
        :return: None
        :rtype: None
        """
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0.0  # Initial score
        self.score_player2 = 0.0

    def record_result(self) -> None:
        """
        Records the result of the match.

        :return: None
        :rtype: None
        """
        pass  # The result is already recorded in MatchController

    def __str__(self) -> str:
        """
        Returns a string representation of the match.

        :return: String representation of the match
        :rtype: str
        """
        return f"{self.player1} (Score: {self.score_player1}) vs {self.player2} (Score: {self.score_player2})"

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Match instance to a dictionary for JSON saving.

        :return: Dictionary representation of the match
        :rtype: Dict[str, Any]
        """
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "score_player1": self.score_player1,
            "score_player2": self.score_player2
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Match':
        """
        Creates a Match instance from a dictionary.

        :param data: Dictionary containing match data
        :type data: Dict[str, Any]
        :return: Match instance
        :rtype: Match
        """
        player1 = Player.from_dict(data["player1"])
        player2 = Player.from_dict(data["player2"])
        match = cls(player1, player2)
        match.score_player1 = data["score_player1"]
        match.score_player2 = data["score_player2"]
        return match
