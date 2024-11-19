# views/match_view.py

class MatchView:
    @staticmethod
    def afficher_match(match):
        print(f"{match.joueur1} vs {match.joueur2}")

    @staticmethod
    def demander_resultat_match(joueur1, joueur2):
        print(f"Match entre {joueur1} et {joueur2}")
        resultat = input("Qui a gagné ? (1 pour Joueur 1, 2 pour Joueur 2, N pour nul) : ")
        return resultat
