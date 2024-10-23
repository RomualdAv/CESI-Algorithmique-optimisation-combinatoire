import uuid

from .Depot import Depot
from .Size import Size
from .TypeBox import TypeBox

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
    def __init__(self, id_box: uuid.UUID,destination: Depot, size: Size,type_box: TypeBox):
        if not isinstance(id_box, uuid.UUID) or not isinstance(destination, Depot) or not isinstance(size, Size) or not isinstance(type_box, TypeBox):
            raise AttributeError("Parameter aren't good type")
        self.__id_box= id_box
        self.__destination= destination
        self.__size= size
        self.__type = type_box
    """
    This method returns the ID of the box.
    """
    def getIdBox(self) -> uuid.UUID:
        return self.__id_box
    """
    This method returns the destination of the box.
    """
    def getDestination(self) -> Depot:
        return self.__destination
    """
    This method returns the size of the box.
    """
    def getSize(self) -> Size:
        return self.__size
    """
    This method returns the type of the box.
    """
    def getLocation(self) -> TypeBox:
        return self.__type

    def __str__(self):
        return f"Box ID: {self.__id_box}, Destination:{self.__destination.getName},size: { self.__size}, DeliveryWindow: { self.__destination.getDeliveryWindow}, Type: {self.__type.name}"
    
        
       