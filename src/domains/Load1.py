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
        self.truck_box_types = {}

    def sortByType(boxes: [Box]) -> dict:
    order = dict()  
    for box in boxes:
        box_type = box.getLocation()  
        type_name = box_type.getName()  
        # Vérifier si le type de boîte n'est pas dans le dictionnaire
        if type_name not in order:
            order[type_name] = []  
        
        # Ajouter la boîte à la liste correspondante
        order[type_name].append(box)
    
    return order  # Retourner le dictionnaire trié
   
       