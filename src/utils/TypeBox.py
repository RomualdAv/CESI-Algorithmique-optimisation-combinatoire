from enum import Enum

from .error import UncreatedTypeError

"""
This class is an enumeration of the types of boxes.
"""
class TypeBox(Enum):
    NOTSPECIFY = 0
    ALIMENTAL = 1
    FLAMMABLE = 2
    EXPLOSIVE = 3
    TOXIC = 4
    RADIOACTIVE = 5
    CORROSIVE = 6
    OXIDIZING = 7
    PRESSURIZED = 8
    FRAGILE = 9

    """
    The method isPossibleToTransport checks if the box can be transported with the other boxes.
    """
    def isPossibleToTransport(self, listtypebox: list) -> bool:
        if not any(elem in listtypebox for elem in listNotPossible[self.value]):
            return True
        else:
            return False
    """
    This method returns the name of the type of box.
    """
    def __str__(self):
        return self.name

listNotPossible = (
        (),
        (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
         TypeBox.OXIDIZING, TypeBox.PRESSURIZED),
        (TypeBox.ALIMENTAL, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
         TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
         TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
         TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.OXIDIZING,
         TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
         TypeBox.PRESSURIZED, TypeBox.FRAGILE),
        (TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
         TypeBox.OXIDIZING, TypeBox.FRAGILE),
        (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
         TypeBox.OXIDIZING, TypeBox.PRESSURIZED)
    )