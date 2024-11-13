from typing import Union
import re


class Joueur:
    def __init__(self, nom: str, prenom: str, date_naissance: str, id_national: Union[int, str]):
        # Le constructeur initialise les attributs de l'instance
        self.nom: str = nom
        self.prenom: str = prenom
        self.id_national: Union[int, str] = id_national
        self.points: int = 0  # Initialise les points à 0

        # Validation du format de la date de naissance
        if not re.match(r'\d{2}/\d{2}/\d{4}', date_naissance):
            raise ValueError(
                "La date de naissance doit être au format jj/mm/aaaa")
        self.date_naissance: str = date_naissance
        
    def __str__(self):
        return f"{self.prenom} {self.nom})"
    
    def mettre_a_jour_points(self, points_gagnes):
        """Met à jour les points du joueur."""
        self.points += points_gagnes
        
    # Exemple de méthode pour afficher les informations du joueur
    def afficher_informations(self) -> None:
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Date de naissance: {self.date_naissance}, ID national: {self.id_national}")

    def to_dict(self):
        """Convertit l'instance en dictionnaire pour la sauvegarde en JSON."""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "id_national": self.id_national,
            "points": self.points
        }

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Joueur à partir d'un dictionnaire."""
        # cls fait référence à la classe Joueur (équivalent de self pour les instances)
        return cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data["date_naissance"],
            id_national=data["id_national"]
        )