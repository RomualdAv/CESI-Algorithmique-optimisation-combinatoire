from uuid import UUID
from .Size import Size
from .Types import TypeTruck
from .Box import Box
from .error import BoxIDError

class Truck:
    """
    This class represents a Truck object.

    Attributes:
        - name (str) : Truck Name
        - size (Size): Stockage capacity
        - type (TypeTruck): Truck type
        - fret (Array<Box>): Boxes list that are contained

        Define a Truck object which can contain multiple boxes
    """
    def __init__(self, name:str, size:Size, truck_type:TypeTruck):
        self.__name = name
        self.__size = size
        self.__type = truck_type
        self.__fret = set()

    def get_name(self)->str:
        """
        Method that return the truck
        """
        return self.__name
    
    def get_size(self)->Size:
        """
        Method that return the truck size
        """
        return self.__size
    
    def get_type(self)->TypeTruck:
        """
        Method that return the truck type
        """
        return self.__type

    def get_fret(self)->set[Box]:
        """
        Method that return the truck boxes
        """
        return set(self.__fret)

    def get_current_weight(self)->int:
        """Method that return the total weight the truck is currently transporting"""
        if not self.__fret:
            return 0
        else:
            return sum(box.get_size().getVolume() for box in self.__fret)

    def can_contain(self, box:Box) -> bool:
        """
        Method that return a boolean value to know if a box size < truck capacity

        :param box: Box object to check if it can be contained in the truck
        """
        return box.get_size().getVolume() <= (self.__size.getVolume() - self.get_current_weight())

    def is_full(self) -> bool:
        """Method that return a boolean value to know if the truck is full"""
        return self.__size.getVolume() == self.get_current_weight()

    def convey_box(self, id_box:UUID):
        """
        Method that substracte a box from the truck

        :param id_box: Box ID to remove from the truck
        """
        for box in self.__fret:
            if box.get_id_box() == id_box:
                self.__fret.remove(box)
                return
        raise BoxIDError(f"{id_box} not found")

    def add_fret(self, fret:Box):
        """
        Methot that add a new set of boxes in the truck

        :param fret: Box object to add in the truck
        """
        self.__fret.add(fret)