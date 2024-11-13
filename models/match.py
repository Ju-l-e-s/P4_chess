from models.joueur import Joueur
import random

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = 0  # Par défaut, les scores sont à 0
        self.score_joueur2 = 0

    def creer_matchs(self, liste_joueurs):
        # 1. Mélanger ou trier les joueurs selon le tour
        if self.nom == "Round 1":
            random.shuffle(liste_joueurs)  # Mélanger pour le premier tour
        else:
            # Trier par points pour les tours suivants
            liste_joueurs.sort(key=lambda joueur: joueur.points, reverse=True)
            # Mélanger les joueurs ayant le même nombre de points
            # (pour cette partie, tu pourrais regrouper les joueurs par score et mélanger chaque groupe)

        # 2. Créer un ensemble ou un dictionnaire pour suivre les paires déjà jouées
        # Par exemple, tu pourrais stocker les paires sous forme de tuples triés (joueur1, joueur2)
        paires_deja_jouees = set()

        # 3. Appairer les joueurs
        self.matchs = []
        i = 0
        while i < len(liste_joueurs) - 1:
            joueur1 = liste_joueurs[i]
            joueur2 = liste_joueurs[i + 1]

            # Vérifie si cette paire a déjà joué ensemble
            if (joueur1, joueur2) in paires_deja_jouees or (joueur2, joueur1) in paires_deja_jouees:
                # Si la paire a déjà joué, essaie avec le joueur suivant
                i += 1
                if i + 1 < len(liste_joueurs):
                    joueur2 = liste_joueurs[i + 1]
                else:
                    break  # Fin de la liste des joueurs

            # Créer le match et enregistrer la paire
            match = Match(joueur1, joueur2)
            self.matchs.append(match)
            paires_deja_jouees.add((joueur1, joueur2))
            i += 2  # Passe à la paire suivante

        # 4. Gérer le cas d'un joueur sans adversaire (impair)
        if len(liste_joueurs) % 2 != 0:
            joueur_restant = liste_joueurs[-1]
            print(f"{joueur_restant} n'a pas d'adversaire pour ce tour (bye).")

        return self.matchs

    def enregistrer_resultat(self):
        """
        Demande le résultat du match et attribue les scores automatiquement.
        """
        print(f"Match entre {self.joueur1} et {self.joueur2}")
        resultat = input(
            "Qui a gagné ? (1 pour Joueur 1, 2 pour Joueur 2, N pour nul) : ")

        if resultat == "1":
            self.score_joueur1 = 1
            self.score_joueur2 = 0
            print(f"{self.joueur1} gagne le match.")
        elif resultat == "2":
            self.score_joueur1 = 0
            self.score_joueur2 = 1
            print(f"{self.joueur2} gagne le match.")
        elif resultat.upper() == "N":
            self.score_joueur1 = 0.5
            self.score_joueur2 = 0.5
            print("Match nul.")
        else:
            print("Entrée invalide. Essayez encore.")
            return self.enregistrer_resultat()  # Relance la demande si entrée incorrecte

        # Mise à jour des points des joueurs
        self.joueur1.mettre_a_jour_points(self.score_joueur1)
        self.joueur2.mettre_a_jour_points(self.score_joueur2)

    def __str__(self):
        return f"{self.joueur1} (Score: {self.score_joueur1}) vs {self.joueur2} (Score: {self.score_joueur2})"

    def to_dict(self):
        """Convertit l'instance de Match en dictionnaire pour la sauvegarde en JSON."""
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "score_joueur1": self.score_joueur1,
            "score_joueur2": self.score_joueur2
        }

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Match à partir d'un dictionnaire."""
        joueur1 = Joueur.from_dict(data["joueur1"])
        joueur2 = Joueur.from_dict(data["joueur2"])
        match = cls(joueur1, joueur2)
        match.score_joueur1 = data["score_joueur1"]
        match.score_joueur2 = data["score_joueur2"]
        return match