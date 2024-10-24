from uuid import UUID
from .Size import Size
from .TypeTruck import TypeTruck
from .Box import Box
from .error import TruckError, BoxIDError

"""
This class represents a Truck object.

Attributes:
    name (str) : Truck Name
    size (Size): Stockage capacity
    type (TypeTruck): Truck type
    fret (Array<Box>): Boxes list that are contained

    Define a Truck object which can contain multiple boxes
"""

class Truck:
    def __init__(self, name:str, size:Size, truck_type:TypeTruck):
        self.__name = name
        self.__size = size
        self.__type = truck_type
        self.__fret = set()
    
    """Get methods"""
    def get_name(self)->str:
        return self.__name
    
    def get_size(self)->Size:
        return self.__size
    
    def get_type(self)->TypeTruck:
        return self.__type

    def get_fret(self)->set:
        return set(self.__fret)

    """Method that return the total weight the truck is currently transporting"""
    def getCurrentWeight(self)->int:
        if not self.__fret:
            raise TruckError("Truck does not contain any fret")
        else:
            return sum(box.getSize().getVolume() for box in self.__fret)

    """Method that return a boolean value to know if a box size < truck capacity"""
    def canContain(self, box:Box) -> bool:
        return box.getSize().getVolume() <= (self.__size.getVolume() - self.getCurrentWeight())

    """Method that return a boolean value to know if the truck is full"""
    def isFull(self) -> bool:
        return self.__size.getVolume() == self.getCurrentWeight()
    
    """Method that substracte a box from the truck"""
    def conveyBox(self, id_box:UUID):
        for box in self.__fret:
            if box.getIdBox() == id_box:
                self.__fret.remove(box)
                return
        raise BoxIDError(f"{id_box} not found")
    
    """Methot that add a new set of boxes in the truck"""
    def addFret(self, fret:Box):
        self.__fret.add(fret)