# controllers/match_controller.py

from views.match_view import MatchView

class MatchController:
    def __init__(self, match):
        self.match = match

    def jouer_match(self):
        # Afficher le match
        MatchView.afficher_match(self.match)
        # Demander le résultat
        resultat = MatchView.demander_resultat_match(self.match.joueur1, self.match.joueur2)
        self.enregistrer_resultat(resultat)

    def enregistrer_resultat(self, resultat):
        if resultat == "1":
            self.match.score_joueur1 = 1
            self.match.score_joueur2 = 0
        elif resultat == "2":
            self.match.score_joueur1 = 0
            self.match.score_joueur2 = 1
        elif resultat.upper() == "N":
            self.match.score_joueur1 = 0.5
            self.match.score_joueur2 = 0.5
        else:
            print("Entrée invalide. Veuillez réessayer.")
            return self.jouer_match()
        # Mettre à jour les points des joueurs
        self.match.joueur1.points += self.match.score_joueur1
        self.match.joueur2.points += self.match.score_joueur2
