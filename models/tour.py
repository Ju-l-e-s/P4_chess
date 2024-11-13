from datetime import datetime
from models.match import Match

class Tour:
    def __init__(self, nom: str):
        self.nom: str = nom
        self.date_heure_debut: datetime = datetime.now()
        self.date_heure_fin: datetime = None
        self.matchs: list = []

    def afficher_informations(self) -> None:
        date_heure_debut_str = self.date_heure_debut.strftime("%d/%m/%Y %H:%M")
        date_heure_fin_str = self.date_heure_fin.strftime(
            "%d/%m/%Y %H:%M") if self.date_heure_fin else "En cours"
        liste_matchs = ', '.join(str(match) for match in self.matchs)
        print(f"Nom: {self.nom}, Date et heure de début: {date_heure_debut_str}, "
              f"Date et heure de fin: {date_heure_fin_str}, Matchs: [{liste_matchs}]")

    def terminer(self, tournoi) -> None:
        self.date_heure_fin = datetime.now()
        # Enregistrer les résultats des matchs
        for match in self.matchs:
            match.enregistrer_resultat()
        # Vérifier si le tournoi est terminé
        if tournoi.tour_actuel >= tournoi.nb_tours:
            tournoi.terminer()

    def creer_matchs(self, liste_joueurs, paires_deja_jouees):
        """
        Crée les matchs pour le tour en évitant les paires déjà jouées
        Crée une liste des paires créer pour éviter de les doublons 
        """
        i = 0
        while i < len(liste_joueurs) - 1:
            joueur1 = liste_joueurs[i]
            joueur2 = liste_joueurs[i + 1]

            # Vérifier si la paire a déjà joué ensemble
            paire = (joueur1.id_national, joueur2.id_national)
            if paire in paires_deja_jouees or (paire[::-1] in paires_deja_jouees):
                # Trouver un autre adversaire
                j = i + 2
                while j < len(liste_joueurs):
                    joueur2 = liste_joueurs[j]
                    nouvelle_paire = (joueur1.id_national, joueur2.id_national)
                    if nouvelle_paire not in paires_deja_jouees and (nouvelle_paire[::-1] not in paires_deja_jouees):
                        # Échanger les joueurs pour éviter la paire déjà jouée
                        liste_joueurs[i + 1], liste_joueurs[j] = liste_joueurs[j], liste_joueurs[i + 1]
                        break
                    j += 1
                else:
                    print(f"Impossible de trouver un adversaire non rencontré pour {joueur1.nom}")
            # Créer le match
            match = Match(joueur1, joueur2)
            self.matchs.append(match)
            # Ajouter la paire aux paires déjà jouées
            paires_deja_jouees.add(paire)
            i += 2

        # Gérer le cas d'un joueur sans adversaire (nombre impair de joueurs)
        if len(liste_joueurs) % 2 != 0:
            joueur_restant = liste_joueurs[-1]
            print(f"{joueur_restant.nom} n'a pas d'adversaire pour ce tour (bye).")

    def to_dict(self):
        """Convertit l'instance en dictionnaire pour la sauvegarde en JSON."""
        return {
            "nom": self.nom,
            "date_heure_debut": self.date_heure_debut.strftime('%d/%m/%Y %H:%M:%S'),
            "date_heure_fin": self.date_heure_fin.strftime('%d/%m/%Y %H:%M:%S') if self.date_heure_fin else None,
            "matchs": [match.to_dict() for match in self.matchs]
        }

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Tour à partir d'un dictionnaire."""
        tour = cls(nom=data["nom"])
        tour.date_heure_debut = datetime.strptime(data["date_heure_debut"], '%d/%m/%Y %H:%M:%S')
        tour.date_heure_fin = datetime.strptime(data["date_heure_fin"], '%d/%m/%Y %H:%M:%S') if data["date_heure_fin"] else None
        tour.matchs = [Match.from_dict(match_data) for match_data in data["matchs"]]
        return tour
