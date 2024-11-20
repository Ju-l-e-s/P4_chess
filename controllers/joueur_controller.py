from models.joueur_model import Joueur
from views.joueur_view import JoueurView

class JoueurController:
    def __init__(self) -> None:
        """
        Initialize the JoueurController by loading the players.

        :return: None
        :rtype: None
        """
        self.joueurs = Joueur.charger_joueurs()

    def ajouter_joueur(self) -> None:
        """
        Add a new player by asking for their information and
        :raises ValueError: If the input information is invalid.
        :return: None
        """
        while True:
            try:
                nom: str
                prenom: str
                date_naissance: str
                id_national: str
                nom, prenom, date_naissance, id_national = JoueurView.demander_informations_joueur()
                joueur = Joueur(nom, prenom, date_naissance, id_national)
                nom, prenom, date_naissance, id_national = JoueurView.demander_informations_joueur()
                joueur = Joueur(nom, prenom, date_naissance, id_national)
                self.joueurs.append(joueur)
                Joueur.sauvegarder_joueurs(self.joueurs)
                print("Joueur ajouté avec succès.")
                break  # Sortir de la boucle si tout va bien
            except ValueError as e:
                print(f"Erreur : {e}")
                print("Veuillez réessayer.")

    def lister_joueurs(self) -> None:
        """
        List all players sorted by their last name.

        :return: None
        :rtype: None
        """
        self.joueurs = Joueur.charger_joueurs()
        self.joueurs.sort(key=lambda j: j.nom)
        JoueurView.afficher_joueurs(self.joueurs)
        
    def lister_joueurs_alphabetique(self) -> None:
        """
        List all players sorted alphabetically by their last name and first name.

        :return: None
        :rtype: None
        """
        self.joueurs = Joueur.charger_joueurs()
        self.joueurs.sort(key=lambda j: (j.nom, j.prenom))
        JoueurView.afficher_joueurs(self.joueurs)