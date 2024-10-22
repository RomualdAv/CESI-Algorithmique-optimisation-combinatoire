import uuid

from src.utils.DeliveryWindow import DeliveryWindow
from src.utils.Depot import Depot
from src.utils.Size import Size
from src.utils.TypeBox import TypeBox

"""
This class represents a Box object.

Attributes:
    id_box (UUID): Box ID
    destination (Depot): Destination of the box
    size (Size): Size of the box
    delivery_window (DeliveryWindow): Delivery window of the box
    type (TypeBox): Type of the box
"""
class Box:
    def __init__(self, id_box: uuid.UUID,destination: Depot, size: Size, delivery_window: DeliveryWindow,type_box: TypeBox):
        self.id_box= id_box
        self.destination= destination 
        self.size= size
        self.delivery_window= delivery_window
        self.type = type_box 
    
    def __str__(self):
        return f"Box ID: {self.id_box}, Destination:{self.destination.name},size: { self.size}, DeliveryWindow: { self.delivery_window}, Type: {self.type.name}"
    
        
       