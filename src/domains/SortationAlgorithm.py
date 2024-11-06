import datetime
import sys
import uuid
from typing import Dict, List
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

    def sortByType(boxes:[Box]) -> dict:

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
   

    def sortboxtime (self, dict_boites: Dict[str, List['Box']]) -> Dict[str, List['Box']]:

        for key, boites in dict_boites.items():
          
            boites.sort(key=lambda box: (box.getEnd(), -box.getDuration().total_seconds()))
            
        return dict_boites
    
    def canLoadAllBoxes(boxes: [Box], trucks: [Truck]) -> bool:
        total_box_volume = sum(box.getSize().getVolume() for box in boxes)  
        total_truck_volume = sum(truck.get_size().getVolume() for truck in trucks)  
    
   
        if total_box_volume <= total_truck_volume:
            return True  
        else:
            return False  
       

