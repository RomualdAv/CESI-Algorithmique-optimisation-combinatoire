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


class Load1:
    def __init__(self):
        # Dictionnaire pour stocker les types de camions et les types de boîtes
        self.truck_box_types = {}

    def manage_box(self, box: Box, truck: Truck):
        """
        Gère l'ajout d'une boîte au chargement en vérifiant si le type de boîte
        correspond au type de camion. Si le type de boîte n'existe pas pour le camion,
        il est ajouté avec une liste vide.
        """
        #1-Récupère le type de la boîte
        box_type = box.getLocation()    # type de boites
        truck_type = truck.get_type()  # Type du camion

        # Vérifie si le type de camion existe déjà dans le dictionnaire
        if truck_type not in self.truck_box_types:
            self.truck_box_types[truck_type] = {}  # Initialiser avec un dictionnaire vide

        # Si le type de boîte n'existe pas pour ce camion, l'ajouter
        if box_type not in self.truck_box_types[truck_type]:
            self.truck_box_types[truck_type][box_type] = {
                'count': 0,
                'boxes': []
            }
            print(f"Box type '{box_type.name}' added for truck type '{truck_type.name}'.")

        # Incrémente le compteur et ajoute la boîte à la liste
        self.truck_box_types[truck_type][box_type]['count'] += 1
        self.truck_box_types[truck_type][box_type]['boxes'].append(box)
        print(f"Box {box.getIdBox()} added to truck type '{truck_type.name}' under box type '{box_type.name}'. Total count: {self.truck_box_types[truck_type][box_type]['count']}.")

        # Ajoute la boîte au fret du camion: Cette ligne met à jour l'état interne du camion en ajoutant la boîte à sa cargaison.
        truck.addFret([box])

   