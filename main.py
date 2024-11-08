from datetime import date
from models.tournoi import Tournoi
from models.joueur import Joueur
import sys


def main():
    # Création d'une liste de 12 joueurs
    joueurs = [
        Joueur(nom="Kevin", prenom="Jean",
               date_naissance="01/01/1990", id_national="AB12345"),
        Joueur(nom="Dupont", prenom="Marie",
               date_naissance="15/03/1985", id_national="CD67890"),
        Joueur(nom="Martin", prenom="Paul",
               date_naissance="22/07/1992", id_national="EF11223"),
        Joueur(nom="Bernard", prenom="Alice",
               date_naissance="30/08/1988", id_national="GH44556"),
        Joueur(nom="Durand", prenom="Luc",
               date_naissance="12/12/1991", id_national="IJ77889"),
        Joueur(nom="Leroy", prenom="Emma",
               date_naissance="05/05/1993", id_national="KL99001"),
        Joueur(nom="Moreau", prenom="Louis",
               date_naissance="20/11/1987", id_national="MN22334"),
        Joueur(nom="Simon", prenom="Chloe",
               date_naissance="25/09/1990", id_national="OP55667"),
        Joueur(nom="Michel", prenom="Pierre",
               date_naissance="10/10/1986", id_national="QR88990"),
        Joueur(nom="Garcia", prenom="Laura",
               date_naissance="18/04/1994", id_national="ST11223"),
        Joueur(nom="Petit", prenom="Antoine",
               date_naissance="07/07/1989", id_national="UV44556"),
        Joueur(nom="Roux", prenom="Julie",
               date_naissance="03/03/1992", id_national="WX77889")
    ]

    # Création d'une liste de tours (vide pour cet exemple)
    tours = []

    # Création d'une instance de Tournoi
    tournoi = Tournoi(
        nom="Championnat",
        lieu="Paris",
        date_debut="01/10/2023",
        date_fin="13/10/2023",
        nb_tours=5,
        tour_actuel=1,
        #joueurs=[],  # Initialement vide
        joueurs=joueurs,  # Initialement vide

        tours=tours,
        description="Tournoi annuel"
    )

    # Ajout des joueurs au tournoi
    # for joueur in joueurs:
    #     tournoi.ajouter_joueur(joueur)

    # Affichage des informations du tournoi après ajout des joueurs
    # tournoi.afficher_informations()
    
    joueurs_melanges = tournoi.liste_joueurs_aléatoire()
    print("Liste des joueurs mélangés :")
    for joueur in joueurs_melanges:
        print(joueur)
        
    # Fermer le script après les impressions
    sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrompu par l'utilisateur.")
