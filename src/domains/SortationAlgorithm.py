from src.domains import InstanceError
from src.domains.SolutionChecker import is_solvable
from src.utils.Box import Box
from src.utils.Truck import Truck
from src.utils.Types import typeOfTruckToUse


def __find_same_depot__(truck: Truck, boxes: list[Box], new_box: Box):
    """
    Find the box that has the same depot as the box in parameter.

    :param truck: The truck try to add boxes.
    :param boxes: The list of boxes to load.
    :param new_box: The box load.
    """

    for box in boxes:
        if new_box.get_destination().get_location() == box.get_destination().get_location():
            if truck.get_type() in typeOfTruckToUse(box.get_type()):
                if truck.can_contain(box):
                    truck.add_fret(box)
                    boxes.remove(box)


class SortationAlgorithm:

    def __init__(self, boxes: list[Box], trucks: list[Truck], graph: list[list[float]]):
        """
        Constructeur de la classe SortationAlgorithm.

        :param boxes: List of boxes to deliver.
        :param trucks: List of trucks to deliver the boxes.
        :param graph: Graphe représentant les distances entre les points de livraison.

        :raises InstanceError: If the problem is not solvable.
        """

        self.__boxes = boxes
        self.__trucks = trucks
        self.__graph = graph
        self.__dict_type = {}

    def __sortByType(self) -> dict:
        """
        Sort the boxes by type.
        """
        if len(self.__dict_type) != 0:
            return self.__dict_type
        order = dict()  
        for box in self.__boxes:
            type_name = box.get_type().name
            # Check if the type of the box is already in the dictionary
            if type_name not in order:
                order[type_name] = []
        
            # Add the box to the list of boxes of the same type
            order[type_name].append(box)
        self.__dict_type = order

        return order

    def __checkContainability(self) -> bool:
        """
        Check if the boxes can be delivered by the trucks.

        :raises InstanceError: If the problem is not solvable.
        :return bool: True if the boxes can be delivered by the trucks.
        """
        list_type = []
        for key, boites in self.__sortByType().items():
            list_type.append(key)

        for truck in self.__trucks:
            type_truck = truck.get_type()
            list_type_copy = list_type[:]
            for type_box_name in list_type_copy:
                type_box = (self.__dict_type[type_box_name])[0].get_type()
                if type_truck in typeOfTruckToUse(type_box):
                    list_type.remove(type_box_name)

        if len(list_type) > 0:
            raise InstanceError("The boxes can't be delivered by the trucks because the truck types are not compatible with the box types.")

        return True

    def getTruckLoaded(self) -> list[Truck]:
        """
        Return the list of trucks loaded.

        :raises InstanceError: If the problem is not solvable.
        """

        # Check if the problem is solvable
        is_solvable(self.__trucks, self.__boxes, self.__graph)
        # Sort the boxes by type
        self.__sortByType()
        # Check if the boxes can be delivered by the trucks
        self.__checkContainability()

        # Check if the problem is solved
        if self.__trucks[0].get_current_weight() != 0:
            return self.__trucks

        # Sort the boxes by decreasing coupling
        for key,boxes in self.__dict_type.items():
            boxes.sort(key=lambda box: box.getCoupling(), reverse=True)
        # Sort the truck by crescent coupling
        self.__trucks.sort(key=lambda truck: truck.getCoupling())

        #Load truck
        for truck in self.__trucks:
            for key,boxes in self.__dict_type.items():
                for box in boxes:
                    if truck.get_type() in box.get_type().typeOfTruckToUse():
                        if truck.can_contain(box):
                            truck.add_fret(box)
                            boxes.remove(box)
                            __find_same_depot__(truck, boxes, box)

        #Check if all boxes are loaded in the trucks

        return self.__trucks