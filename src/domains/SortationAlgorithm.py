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

        types_keys = list(self.__dict_type.keys())

        # Sort the type boxes by decreasing coupling
        types_keys.sort(key=lambda key: getBoxCoupling(self.__dict_type[key][0].get_type()), reverse=True)
        # Sort the truck by crescent coupling
        self.__trucks.sort(key=lambda truck: getTruckCoupling(truck.get_type()))

        #Load truck
        for truck in self.__trucks:
            for key in types_keys[:]:
                boxes = self.__dict_type[key]
                for box in boxes:
                    if truck.get_type() in typeOfTruckToUse(box.get_type()):
                        if truck.can_contain(box):
                            truck.add_fret(box)
                            boxes.remove(box)
                            __find_same_depot__(truck, boxes, box)
                    if len(boxes) == 0:
                        types_keys.remove(key)
                        break
                if truck.is_full():
                    break

        self.__reorganize_trucks(types_keys)

        return self.__trucks

    def __remove_incompatible_boxes(self, truck: Truck, box_type: TypeBox, types_remaining: list[str]):
        """
        Remove incompatible boxes from the truck to make space for a box of the given type.

        :param truck: The truck from which to remove incompatible boxes.
        :param box_type: The type of the box that needs to be loaded.
        :param types_remaining: The types of boxes that couldn't be loaded initially.
        """
        incompatible_boxes = [box for box in truck.get_fret() if not is_compatible(box.get_type(), box_type)]
        for box in incompatible_boxes:
            truck.convey_box(box.get_id_box())
            type_name = box.get_type().name

            if type_name not in self.__dict_type:
                self.__dict_type[type_name] = []
                types_remaining.append(type_name)
                types_remaining.sort(key=lambda key: getBoxCoupling(self.__dict_type[key][0].get_type()), reverse=True)

            self.__dict_type[type_name].append(box)

    def __reorganize_trucks(self, types_remaining: list[str]):
        """
        Reorganize the trucks to load the boxes that couldn't be loaded initially.

        :param types_remaining: The types of boxes that couldn't be loaded initially.
        """
        truck_not_rework = self.__trucks.copy()
        for key in types_remaining:
            if len(self.__dict_type[key]) == 0:
                del self.__dict_type[key]
                continue
            for truck in [truck for truck in truck_not_rework if truck.get_type() in typeOfTruckToUse(self.__dict_type[key][0].get_type())]:
                for box in self.__dict_type[key]:
                    self.__remove_incompatible_boxes(truck, box.get_type(),types_remaining)
                    if truck.can_contain(box):
                        truck.add_fret(box)
                        self.__dict_type[key].remove(box)
                        truck_not_rework.remove(truck)
                        break

        if len(self.__dict_type) != 0:
            raise InstanceError("The boxes can't be delivered by the trucks because the boxes can't be loaded in the trucks")

        return self.__trucks