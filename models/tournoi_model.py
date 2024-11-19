# models/tournoi.py

from datetime import datetime
from models.tour_model import Tour
from models.joueur_model import Joueur
import json
import os

class Tournoi:
    data_file = 'data/tournois.json'

    def __init__(self, nom, lieu, nb_tours=4, description=''):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = datetime.now().strftime('%d/%m/%Y')  # Date actuelle
        self.date_fin = None  # Sera définie à la fin du tournoi
        self.nb_tours = nb_tours
        self.tour_actuel = 0
        self.joueurs = []
        self.tours = []
        self.description = description
        self.paires_deja_jouees = set()

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_tour(self, tour):
        self.tours.append(tour)
        self.tour_actuel += 1
        
    def get_classement(self):
        # Créer une liste des joueurs avec leurs points
        classement = sorted(self.joueurs, key=lambda joueur: joueur.points, reverse=True)
        return classement
    
    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'nb_tours': self.nb_tours,
            'tour_actuel': self.tour_actuel,
            'joueurs': [joueur.to_dict() for joueur in self.joueurs],
            'tours': [tour.to_dict() for tour in self.tours],
            'description': self.description,
            'paires_deja_jouees': list(self.paires_deja_jouees)
        }
        
    def terminer(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y')
    
    @classmethod
    def from_dict(cls, data):
        tournoi = cls(
            nom=data['nom'],
            lieu=data['lieu'],
            nb_tours=data.get('nb_tours', 4),
            description=data.get('description', '')
        )
        tournoi.date_debut = data['date_debut']
        tournoi.date_fin = data.get('date_fin')  # Peut être None
        tournoi.tour_actuel = data.get('tour_actuel', 0)
        tournoi.joueurs = [Joueur.from_dict(j) for j in data.get('joueurs', [])]
        tournoi.tours = [Tour.from_dict(t) for t in data.get('tours', [])]
        tournoi.paires_deja_jouees = set(tuple(paire) for paire in data.get('paires_deja_jouees', []))
        return tournoi


    @classmethod
    def sauvegarder_tournois(cls, liste_tournois):
        with open(cls.data_file, 'w') as f:
            json.dump([tournoi.to_dict() for tournoi in liste_tournois], f, indent=4)

    @classmethod
    def charger_tournois(cls):
        if os.path.exists(cls.data_file):
            with open(cls.data_file, 'r') as f:
                data = json.load(f)
                return [cls.from_dict(tournoi_data) for tournoi_data in data]
        else:
            return []
