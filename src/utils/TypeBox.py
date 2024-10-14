from enum import Enum

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
    
    def __init__(self):
        super().__init__()
        self.__listNotPosible = (
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

    """
    The method isPossibleToTransport checks if the box can be transported with the other boxes.
    """
    def isPossibleToTransport(self, listtypebox):
        if self == TypeBox.ALIMENTAL:
            if not listtypebox.contains(self.__listNotPosible[1]):
                return False
        elif self == TypeBox.FLAMMABLE:
            if not listtypebox.contains(self.__listNotPosible[2]):
                return False
        elif self == TypeBox.EXPLOSIVE:
            if not listtypebox.contains(self.__listNotPosible[3]):
                return False
        elif self == TypeBox.TOXIC:
            if not listtypebox.contains(self.__listNotPosible[4]):
                return False
        elif self == TypeBox.RADIOACTIVE:
            if not listtypebox.contains(self.__listNotPosible[5]):
                return False
        elif self == TypeBox.CORROSIVE:
            if not listtypebox.contains(self.__listNotPosible[6]):
                return False
        elif self == TypeBox.OXIDIZING:
            if not listtypebox.contains(self.__listNotPosible[7]):
                return False
        elif self == TypeBox.PRESSURIZED:
            if not listtypebox.contains(self.__listNotPosible[8]):
                return False
        elif self == TypeBox.FRAGILE:
            if not listtypebox.contains(self.__listNotPosible[9]):
                return False
        return True
    """
    This method returns the name of the type of box.
    """
    def __str__(self):
        return self.name
