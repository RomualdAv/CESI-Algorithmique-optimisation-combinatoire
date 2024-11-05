
import datetime
import sys
import uuid
sys.path.insert(0, '../src')
import unittest
from utils.Box import Box
from utils.Truck import Truck
from utils.Size import Size
from utils.Depot import Depot
from utils.TypeBox import TypeBox
from utils.DeliveryWindow import DeliveryWindow


class Verification_Solvable:
    def verifier_solvabilite_globale(
    camions, boites, villes, itineraire, trafic, fenetres_de_temps,
    priorites=None, couts_par_km=None, restrictions_route=None,
    pauses_conducteurs=None, retour_depot=True
):
        for camion in camions:
            volume_total_boites = sum(boite.volume for boite in boites if boite.camion == camion)
            poids_total_boites = sum(boite.poids for boite in boites if boite.camion == camion)
        
        if volume_total_boites > camion.volume_max or poids_total_boites > camion.poids_max:
            print(f"Capacité dépassée pour le camion {camion.id}")
            return False

    # Vérification des fenêtres de temps et du trafic
        for ville, voisins in itineraire.items():
            for voisin in voisins:
                trajet = calculer_duree_trajet(ville, voisin, trafic)
            if not fenetres_de_temps_compatibles(ville, voisin, trajet, fenetres_de_temps):
                print(f"Fenêtre de temps incompatible entre {ville} et {voisin}")
            return False

    # Priorités de livraison
        if priorites:
            for boite, priorite in priorites.items():
                if not respecter_priorite(boite, priorite, itineraire):
                    print(f"La boîte {boite.id} n'a pas respecté sa priorité de livraison")
                return False

    # Vérification du retour au dépôt
    if retour_depot and not retourner_au_depot(itineraire, villes[0]):
        print("Retour au dépôt initial non respecté")
        return False

    print("L'instance est globalement solvable : toutes les contraintes sont satisfaites.")

def calculer_cout_total(itineraire, camions, couts_par_km):
    # Calcule le coût total en fonction de la distance et du coût par km de chaque camion
    cout = 0
    for camion in camions:
        for ville in itineraire[camion.position]:
            cout += couts_par_km[camion] * distances[ville]
    return cout


# Fonctions auxiliaires fictives
def calculer_duree_trajet(ville_depart, ville_arrivee, trafic):
    return trafic.get((ville_depart, ville_arrivee), 1.0)

def fenetres_de_temps_compatibles(ville_depart, ville_arrivee, duree_trajet, fenetres_de_temps):
    debut, fin = fenetres_de_temps.get(ville_arrivee, (0, 24))
    heure_arrivee = heure_depart + duree_trajet
    return debut <= heure_arrivee <= fin

def respecter_priorite(boite, priorite, itineraire):
    # Vérifie si une boîte prioritaire est livrée en premier
    return True  # Exemple fictif

def retourner_au_depot(itineraire, depot_initial):
    # Vérifie que la tournée revient au point de départ
    return itineraire[-1] == depot_initial