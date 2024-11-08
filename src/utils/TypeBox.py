from .TypeTruck import *

class TypeBox(Enum):
    """
    This class is an enumeration of the types of boxes.
    """
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

    def isPossibleToTransport(self, listtypebox: list) -> bool:
        """
        The method isPossibleToTransport checks if the box can be transported with the other boxes.
        """
        if not any(elem in listtypebox for elem in listNotPossible[self.value]):
            return True
        else:
            return False

    def typeOfTruckToUse(self) -> [TypeTruck]:
        """
        This function returns the type of truck to use.
        """
        type_list = list()
        if not any(elem == self for elem in list_not_possible_truck[0]):
            type_list.append(TypeTruck.OPEN)
        if not any(elem == self for elem in list_not_possible_truck[1]):
            type_list.append(TypeTruck.REFRIGERATE)
        if not any(elem == self for elem in list_not_possible_truck[2]):
            type_list.append(TypeTruck.WATERTIGHT)
        if not any(elem == self for elem in list_not_possible_truck[3]):
            type_list.append(TypeTruck.PLATED)

        return type_list

    def getCoupling(self) -> int:
        """
        This function returns the coupling value of the box.
        Greater are the coupling value, more the box is difficult to transport.
        """
        return len(listNotPossible[self.value])

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