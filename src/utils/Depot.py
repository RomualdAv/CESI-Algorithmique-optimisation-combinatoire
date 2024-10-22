from .DeliveryWindow import DeliveryWindow

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
        self.__location = location
        self.__name= name
        self.__delivery_window= delivery_window # fenetre de livraison
        self.__possibility_of_parking= possibility_of_parking # possibilite de se garer en bool
    """
    This method returns the location of the depot.
    """
    def getLocation(self) -> int:
        return self.__location
    """
    This method returns the name of the depot.
    """
    def getName(self) -> str:
        return self.__name
    """
    This method returns the delivery window of the depot.
    """
    def getDeliveryWindow(self) -> DeliveryWindow:
        return self.__delivery_window
    """
    This method returns the possibility of parking in the depot.
    """
    def getPossibilityParking(self) -> bool:
        return self.__possibility_of_parking

    def __str__(self) -> str:
        return f"Depot : {self.__name}, Location: {self.__location}, Parking:{ 'Yes' if self.__possibility_of_parking else 'No'}, Delivery window: {self.__delivery_window}"
    
       