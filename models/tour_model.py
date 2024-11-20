from datetime import datetime
from models.match_model import Match

class Tour:
    def __init__(self, nom: str):
        """
        Initialize a Tour instance.

        :param nom: The name of the tour.
        :type nom: str
        """
        self.nom: str = nom
        self.date_heure_debut: datetime = datetime.now()
        self.date_heure_fin: datetime = None
        self.matchs: list = []

    def afficher_informations(self) -> None:
        """
        Display the information of the tour.

        :return: None
        :rtype: None
        """
        date_heure_debut_str = self.date_heure_debut.strftime("%d/%m/%Y %H:%M")
        date_heure_fin_str = self.date_heure_fin.strftime(
            "%d/%m/%Y %H:%M") if self.date_heure_fin else "En cours"
        liste_matchs = ', '.join(str(match) for match in self.matchs)
        print(f"Nom: {self.nom}, Date et heure de début: {date_heure_debut_str}, "
              f"Date et heure de fin: {date_heure_fin_str}, Matchs: [{liste_matchs}]")

    def terminer(self, tournoi) -> None:
        """
        End the tour and update the tournament status.

        :param tournoi: The tournament instance.
        :type tournoi: Tournament
        :return: None
        :rtype: None
        """
        self.date_heure_fin = datetime.now()
        # Save the results of the matches
        for match in self.matchs:
            match.enregistrer_resultat()
        # Check if the tournament is finished
        if tournoi.tour_actuel >= tournoi.nb_tours:
            tournoi.terminer()

    def creer_matchs(self, liste_joueurs: list, paires_deja_jouees: set) -> None:
        """
        Create matches for the tour avoiding already played pairs.

        :param liste_joueurs: List of players.
        :type liste_joueurs: list
        :param paires_deja_jouees: Set of already played pairs.
        :type paires_deja_jouees: set
        :return: None
        :rtype: None
        """
        i = 0
        while i < len(liste_joueurs) - 1:
            joueur1 = liste_joueurs[i]
            joueur2 = liste_joueurs[i + 1]

            # Check if the pair has already played together
            paire = (joueur1.id_national, joueur2.id_national)
            if paire in paires_deja_jouees or (paire[::-1] in paires_deja_jouees):
                # Find another opponent
                j = i + 2
                while j < len(liste_joueurs):
                    joueur2 = liste_joueurs[j]
                    nouvelle_paire = (joueur1.id_national, joueur2.id_national)
                    if nouvelle_paire not in paires_deja_jouees and (nouvelle_paire[::-1] not in paires_deja_jouees):
                        # Swap players to avoid the already played pair
                        liste_joueurs[i + 1], liste_joueurs[j] = liste_joueurs[j], liste_joueurs[i + 1]
                        break
                    j += 1
                else:
                    print(f"Impossible de trouver un adversaire non rencontré pour {joueur1.nom}")
            # Create the match
            match = Match(joueur1, joueur2)
            self.matchs.append(match)
            # Add the pair to already played pairs
            paires_deja_jouees.add(paire)
            i += 2

        # Handle the case of a player without an opponent (odd number of players)
        if len(liste_joueurs) % 2 != 0:
            joueur_restant = liste_joueurs[-1]
            print(f"{joueur_restant.nom} n'a pas d'adversaire pour ce tour (bye).")

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary for JSON saving.

        :return: Dictionary representation of the instance.
        :rtype: dict
        """
        return {
            "nom": self.nom,
            "date_heure_debut": self.date_heure_debut.strftime('%d/%m/%Y %H:%M:%S'),
            "date_heure_fin": self.date_heure_fin.strftime('%d/%m/%Y %H:%M:%S') if self.date_heure_fin else None,
            "matchs": [match.to_dict() for match in self.matchs]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Tour':
        """
        Create a Tour instance from a dictionary.

        :param data: Dictionary containing tour data.
        :type data: dict
        :return: Tour instance.
        :rtype: Tour
        """
        tour = cls(nom=data["nom"])
        tour.date_heure_debut = datetime.strptime(data["date_heure_debut"], '%d/%m/%Y %H:%M:%S')
        tour.date_heure_fin = datetime.strptime(data["date_heure_fin"], '%d/%m/%Y %H:%M:%S') if data["date_heure_fin"] else None
        tour.matchs = [Match.from_dict(match_data) for match_data in data["matchs"]]
        return tour
