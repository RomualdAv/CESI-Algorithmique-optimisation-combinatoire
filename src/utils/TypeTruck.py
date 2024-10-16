from enum import Enum
from TypeBox import TypeBox
from error import TruckError

listnotposible = (
            (TypeBox.ALIMENTAL,TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING),
            (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING, TypeBox.PRESSURIZED),
            (TypeBox.RADIOACTIVE,TypeBox.PRESSURIZED),
            ()
        )
"""
This function returns the type of truck to use.
"""
def typeOfTruckToUse(listtypebox):
    if not listtypebox.contains(listnotposible[0]):
        return TypeTruck.OPEN
    elif not listtypebox.contains(listnotposible[1]):
        return TypeTruck.REFRIGERATE
    elif not listtypebox.contains(listnotposible[2]):
        return TypeTruck.WATERTIGHT
    elif not listtypebox.contains(listnotposible[3]):
        return TypeTruck.PLATED

    #Impossible to determine the type of truck
    raise TruckError("Impossible to determine the type of truck")
"""
This class is an enumeration of the types of trucks.
"""
class TypeTruck(Enum):
    OPEN = 0
    REFRIGERATE = 1
    WATERTIGHT = 2
    PLATED = 3

    """
    This method returns the name of the type of truck.
    """

    def __str__(self):
        return self.name
