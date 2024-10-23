from uuid import UUID
from src.utils.Size import Size
from src.utils.TypeTruck import TypeTruck
from src.utils.Box import Box
from src.utils.error import TruckError, BoxIDError

"""
This class represents a Truck object.

Attributes:
    name (str): Truck Name
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
        self.__fret = []
    
    """Get methods"""
    def get_name(self):
        return self.__name
    
    def get_size(self):
        return self.__size
    
    def get_type(self):
        return self.__type

    """Method that return the total weight the truck is currently transporting"""

    def getCurrentWeight(self):
        current_weight = 0
        if self.__fret == []:
            raise TruckError("Truck does not contain any fret")
        else:
            return sum(box.size for box in self.__fret)
    """Method that return a boolean value to know if a box size < truck capacity"""
    def canContain(self, box:Box):
        return box.size <= (self.__size - self.get_current_weight())

    """Method that return a boolean value to know if the truck is full"""
    def isFull(self):
        return self.__size == self.get_current_weight()
    
    """Method that substracte a box from the truck"""
    def conveyBox(self, id_box:UUID):
        for box in self.__fret:
            if box.id_box == id_box:
                self.__fret.remove(box)
                return
        raise BoxIDError(f"{id_box} not found")
    
    """Methot that add a new set of boxes in the truck"""
    def addFret(self, fret:list[Box]):
        if fret is None:
            self.__fret = fret
            return
        raise TruckError("A fret is already set in the truck")