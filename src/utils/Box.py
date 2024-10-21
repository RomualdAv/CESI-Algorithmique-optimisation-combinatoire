import uuid
class box:
    def __init__(self, destination, size, delivery_window,type_box):
        self.id_box= uuid.uuid4() # generation d'identifiant unique pour une boite
        self.destination= destination 
        self.size= size
        self.delivery_window= delivery_window
        self.type = type_box 
    
    def __str__(self):
        return f"Box ID: {self.id_box}, Destination:{self.destination.name},
        size: { self.size}, Delivery window: { self.delivery_window}, Type: {self.type.name}"
    
        
       