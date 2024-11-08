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
        return f"{self.prenom} {self.nom} (Points: {self.points})"
    
    # Exemple de méthode pour afficher les informations du joueur
    def afficher_informations(self) -> None:
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Date de naissance: {self.date_naissance}, ID national: {self.id_national}")

    # Méthode pour mettre à jour les points du joueur
    def mettre_a_jour_points(self, points_gagnes: int) -> None:
        self.points += points_gagnes
