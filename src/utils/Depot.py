from src.utils.DeliveryWindow import DeliveryWindow

"""
This class represents a depot. A depot is a place where the vehicle can park and deliver the goods.

Attributes:
    - location (Vertex): Vertex on the graph
    - name (string): Name of the depot
    - possibility_of_parking (boolean): Possibility of parking
    - delivery_window (DeliveryWindow): When is possibile to deliver the goods
"""
class Depot:
    def __init__(self, location: int, name : str, possibility_of_parking: bool, delivery_window: DeliveryWindow):
        self.location = location 
        self.name= name
        self.delivery_window= delivery_window # fenetre de livraison
        self.possibility_of_parking= possibility_of_parking # possibilite de se garer en bool

    def __str__(self):
        return f"Depot : {self.name}, Location: {self.location}, Parking:{ 'Yes' if self.possibility_of_parking else 'No'}, Delivery window: {self.delivery_window}"
    
       