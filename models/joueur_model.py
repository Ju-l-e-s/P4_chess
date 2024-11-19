# models/joueur.py

import re
import json
import os

class Joueur:
    data_file = 'data/joueurs.json'

    def __init__(self, nom, prenom, date_naissance, id_national):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_national = id_national
        self.points = 0.0  # Utilisation de float pour les demi-points

        # Validation de l'identifiant national
        if not re.match(r'^[A-Z]{2}\d{5}$', self.id_national):
            raise ValueError("L'identifiant national doit être deux lettres suivies de cinq chiffres (ex: AB12345)")

        # Validation du format de la date de naissance
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', self.date_naissance):
            raise ValueError("La date de naissance doit être au format jj/mm/aaaa")
    
    def mettre_a_jour_points(self, points):
        self.points += points
        
    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'id_national': self.id_national,
            'points': self.points
        }

    @classmethod
    def from_dict(cls, data):
        joueur = cls(
            nom=data['nom'],
            prenom=data['prenom'],
            date_naissance=data['date_naissance'],
            id_national=data['id_national']
        )
        joueur.points = data.get('points', 0.0)
        return joueur

    @classmethod
    def sauvegarder_joueurs(cls, liste_joueurs):
        # Vérifier que le répertoire existe, sinon le créer
        directory = os.path.dirname(cls.data_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(cls.data_file, 'w') as f:
            json.dump([joueur.to_dict() for joueur in liste_joueurs], f, indent=4)

    @classmethod
    def charger_joueurs(cls):
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(joueur_data) for joueur_data in data]
        else:
            return []

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.id_national})"
