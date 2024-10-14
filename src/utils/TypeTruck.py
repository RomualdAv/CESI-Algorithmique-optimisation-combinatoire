from enum import Enum
import TypeBox

listNotPosible = (
            (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.PRESSURIZED, TypeBox.FRAGILE),
            (TypeBox.ALIMENTAL, TypeBox.PRESSURIZED, TypeBox.FRAGILE),
            (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.CORROSIVE,
             TypeBox.OXIDIZING, TypeBox.FRAGILE),
            (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE,
             TypeBox.CORROSIVE, TypeBox.OXIDIZING, TypeBox.PRESSURIZED, TypeBox.FRAGILE)
        )
"""
This function returns the type of truck to use.
"""
def typeOfTruckToUse(listtypebox):
    lengthlisttypebox = len(listtypebox)
    if listtypebox.contains(listNotPosible[0] and lengthlisttypebox <= len(listNotPosible[0])):
        return TypeTruck.OPEN
    elif listtypebox.contains(listNotPosible[1] and lengthlisttypebox <= len(listNotPosible[1])):
        return TypeTruck.REFRIGERATE
    elif listtypebox.contains(listNotPosible[2] and lengthlisttypebox <= len(listNotPosible[2])):
        return TypeTruck.WATERTIGHT
    elif listtypebox.contains(listNotPosible[3] and lengthlisttypebox <= len(listNotPosible[3])):
        return TypeTruck.PLATED
    return TypeTruck.OPEN
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
