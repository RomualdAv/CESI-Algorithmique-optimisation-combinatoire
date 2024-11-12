from src.domains import InstanceError
from src.domains.SolutionChecker import is_solvable
from src.utils.Box import Box
from src.utils.Truck import Truck
from src.utils.Types import typeOfTruckToUse, getTruckCoupling, getBoxCoupling, is_compatible, TypeBox


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
            raise InstanceError(
                "The boxes can't be delivered by the trucks because the truck types are not compatible with the box types.")

        return True

    def getTruckLoaded(self) -> list[Truck]:
        """
        Load trucks with boxes according to the specified algorithm.

        :return: List of loaded trucks.
        """
        # Step 1: Initialize lists
        loaded_trucks = []
        remaining_boxes = self.__boxes.copy()

        # Step 2: Sort trucks by capacity and types compatible (ascending order of priority)
        self.__trucks.sort(key=lambda truck: (truck.get_size().getVolume(), getTruckCoupling(truck.get_type())))

        # Step 3: Sort boxes by type and loading priorities (descending order of coupling)
        boxes_by_type = self.__sortByType()

        for type_name in boxes_by_type:
            boxes_by_type[type_name].sort(key=lambda box: getBoxCoupling(box.get_type()), reverse=True)

        # Step 4: Load trucks
        for truck in self.__trucks:
            boites_chargees = []

            for type_name, boxes_of_type in list(boxes_by_type.items()):
                if truck.get_type() in typeOfTruckToUse(boxes_of_type[0].get_type()):
                    for box in boxes_of_type[:]:
                        if truck.can_contain(box):
                            truck.add_fret(box)
                            boxes_of_type.remove(box)
                            boites_chargees.append(box)
                        if not boxes_of_type:
                            del boxes_by_type[type_name]
                            break
                    if truck.is_full():
                        break

            loaded_trucks.append(truck)

        # Step 5: Reorganize if necessary
        for truck in loaded_trucks:
            for type_name, boxes_of_type in list(boxes_by_type.items()):
                if truck.get_type() in typeOfTruckToUse(boxes_of_type[0].get_type()):
                    for box in boxes_of_type[:]:
                        if truck.can_contain(box):
                            truck.add_fret(box)
                            boxes_of_type.remove(box)
                        if not boxes_of_type:
                            del boxes_by_type[type_name]
                            break

        # Step 6: Check for remaining boxes
        remaining_boxes = [box for boxes_of_type in boxes_by_type.values() for box in boxes_of_type]

        # Step 7: Raise error if boxes remain
        if remaining_boxes:
            raise InstanceError("Some boxes couldn't be loaded due to constraints.")

        # Step 8: Return loaded trucks and remaining boxes
        return loaded_trucks