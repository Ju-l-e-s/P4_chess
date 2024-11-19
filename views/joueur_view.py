# views/joueur_view.py

class JoueurView:
    @staticmethod
    def afficher_joueurs(joueurs):
        for joueur in joueurs:
            print(f"{joueur.nom} {joueur.prenom} (ID: {joueur.id_national}) - Points: {joueur.points}")

    @staticmethod
    def demander_informations_joueur():
        nom = input("Nom de famille : ")
        prenom = input("Prénom : ")
        date_naissance = input("Date de naissance (jj/mm/aaaa) : ")
        id_national = input("Identifiant national (ex: AB12345) : ")
        return nom, prenom, date_naissance, id_national
