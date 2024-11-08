from enum import Enum
from .TypeBox import TypeBox

"""
This class is an enumeration of the types of trucks.
"""
class TypeTruck(Enum):
    OPEN = 0
    REFRIGERATE = 1
    WATERTIGHT = 2
    PLATED = 3

    def getCoupling(self) -> int:
        """
        This function returns the coupling value of the truck.
        Greater are the coupling value, less is number of different type can we transport.
        """
        return len(list_not_possible_truck[self.value])

    """
    This method returns the name of the type of truck.
    """
    def __str__(self):
        return self.name

list_not_possible_truck = (
            (TypeBox.ALIMENTAL,TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING),
            (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING, TypeBox.PRESSURIZED),
            (TypeBox.RADIOACTIVE,TypeBox.PRESSURIZED),
            ()
        )