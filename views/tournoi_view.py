class TournoiView:
    @staticmethod
    def afficher_informations_tournoi(tournoi):
        print(f"Tournoi : {tournoi.nom}")
        print(f"Lieu : {tournoi.lieu}")
        print(f"Date de début : {tournoi.date_debut}")
        if tournoi.date_fin:
            print(f"Date de fin : {tournoi.date_fin}")
        else:
            print("Date de fin : En cours")
        print(f"Nombre de tours : {tournoi.nb_tours}")
        print(f"Description : {tournoi.description}")
        
    @staticmethod
    def afficher_classement(joueurs):
        print("\n--- Classement des Joueurs ---")
        for i, joueur in enumerate(joueurs, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} - {joueur.points} points")

    @staticmethod
    def demander_informations_tournoi():
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        nb_tours = input("Nombre de tours (par défaut 4) : ") or '4'
        description = input("Description : ")
        return nom, lieu, nb_tours, description

    @staticmethod
    def afficher_liste_tournois(tournois):
        for tournoi in tournois:
            print(f"- {tournoi.nom} à {tournoi.lieu} du {tournoi.date_debut} au {tournoi.date_fin}")
