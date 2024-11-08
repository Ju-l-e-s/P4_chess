class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = 0  # Par défaut, les scores sont à 0
        self.score_joueur2 = 0

    def enregistrer_resultat(self, score_joueur1, score_joueur2):
        """
        Enregistre le résultat du match.
        :param score_joueur1: Score de joueur1 (0, 0.5 ou 1)
        :param score_joueur2: Score de joueur2 (0, 0.5 ou 1)
        """
        self.score_joueur1 = score_joueur1
        self.score_joueur2 = score_joueur2
        self.joueur1.mettre_a_jour_points(score_joueur1)
        self.joueur2.mettre_a_jour_points(score_joueur2)

    def __str__(self):
        return f"{self.joueur1} (Score: {self.score_joueur1}) vs {self.joueur2} (Score: {self.score_joueur2})"
