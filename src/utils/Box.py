import uuid

from .Depot import Depot
from .Size import Size
from .Types import TypeBox

class Box:
    """
    This class represents a Box object.

    Attributes:
        - id_box: (UUID): Box ID
        - destination: (Depot): Destination of the box
        - size: (Size): Size of the box
        - type: (TypeBox): Type of the box
    """
    def __init__(self, id_box: uuid.UUID,destination: Depot, size: Size,type_box: TypeBox):
        if not isinstance(id_box, uuid.UUID) or not isinstance(destination, Depot) or not isinstance(size, Size) or not isinstance(type_box, TypeBox):
            raise AttributeError("Parameter aren't good type")
        self.__id_box= id_box
        self.__destination= destination
        self.__size= size
        self.__type = type_box

    def get_id_box(self) -> uuid.UUID:
        """
        This method returns the ID of the box.
        """
        return self.__id_box

    def get_destination(self) -> Depot:
        """
        This method returns the destination of the box.
        """
        return self.__destination

    def get_size(self) -> Size:
        """
        This method returns the size of the box.
        """
        return self.__size

    def get_type(self) -> TypeBox:
        """
        This method returns the type of the box.
        """
        return self.__type

    def __str__(self):
        return f"Box ID: {self.__id_box}, Destination:{self.__destination.get_name},size: { self.__size}, Type: {self.__type.name}"
    
        
       