from enum import Enum

class TypeTruck(Enum):
    """
    This class is an enumeration of the types of trucks.
    """
    OPEN = 0
    REFRIGERATE = 1
    WATERTIGHT = 2
    PLATED = 3

    def __str__(self):
        """
        This method returns the name of the type of truck.
        """
        return self.name

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

    def __str__(self):
        return self.name

# This list contains the types of boxes that can't be transported with the type of truck.
list_coupling_truck = (
            (TypeBox.ALIMENTAL,TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING),
            (TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING, TypeBox.PRESSURIZED),
            (TypeBox.RADIOACTIVE,TypeBox.PRESSURIZED),
            ()
        )

# This list contains the types of boxes that can't be transported with the type of box.
list_coupling_boxes = (
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

def getTruckCoupling(type_truck: TypeTruck) -> int:
    """
    This function returns the coupling value of the truck.
    Greater are the coupling value, less is number of different type can we transport.

    :param type_truck: The type of the truck.

    :return int: The coupling value of the truck.
    """
    return len(list_coupling_truck[type_truck.value])

def getBoxCoupling(type_box: TypeBox) -> int:
    """
    This function returns the coupling value of the box.
    Greater are the coupling value, more the box is difficult to transport.

    :param type_box: The type of the box.

    :return int: The coupling value of the box.
    """
    return len(list_coupling_boxes[type_box.value])

def typeOfTruckToUse(type_box: TypeBox) -> list[TypeTruck]:
    """
    This function returns the type of truck to use.

    :param type_box: The type of the box.

    :return list[TypeTruck]: The list of the type of truck to use.
    """
    type_list = list()
    if not any(elem == type_box for elem in list_coupling_truck[0]):
        type_list.append(TypeTruck.OPEN)
    if not any(elem == type_box for elem in list_coupling_truck[1]):
        type_list.append(TypeTruck.REFRIGERATE)
    if not any(elem == type_box for elem in list_coupling_truck[2]):
        type_list.append(TypeTruck.WATERTIGHT)
    if not any(elem == type_box for elem in list_coupling_truck[3]):
        type_list.append(TypeTruck.PLATED)

    return type_list