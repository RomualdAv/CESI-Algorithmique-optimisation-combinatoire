from src.domains import InstanceError
from src.domains.SolutionChecker import is_solvable
from src.utils.Box import Box
from src.utils.Truck import Truck


def __find_same_depot__(truck: Truck, boxes: list[Box], new_box: Box):
    """
    Find the box that has the same depot as the box in parameter.

    :param truck: The truck try to add boxes.
    :param boxes: The list of boxes to load.
    :param new_box: The box load.
    """

    for box in boxes:
        if new_box.getDestination().getLocation() == box.getDestination().getLocation():
            if truck.get_type() in box.getType().typeOfTruckToUse():
                if truck.canContain(box):
                    truck.addFret(box)
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
        self.__dict_type = None

    def __sortByType__(self) -> dict:
        """
        Sort the boxes by type.
        """
        if self.__dict_type is not None:
            return self.__dict_type
        order = dict()  
        for box in self.__boxes:
            type_name = box.getType().name
            # Check if the type of the box is already in the dictionary
            if type_name not in order:
                order[type_name] = []
        
            # Add the box to the list of boxes of the same type
            order[type_name].append(box)
        self.__dict_type = order

        return order

    def __checkContainability__(self) -> bool:
        """
        Check if the boxes can be delivered by the trucks.
        """
        list_type = []
        for key, boites in self.__dict_type.items():
            list_type.append(key)

        for truck in self.__trucks:
            type_truck = truck.get_type()
            for type_box_name in list_type:
                type_box = (self.__dict_type[type_box_name])[0].getType()
                if type_truck in type_box.typeOfTruckToUse():
                    list_type.remove(type_box_name)
                    break

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
        self.__sortByType__()
        # Check if the boxes can be delivered by the trucks
        self.__checkContainability__()

        # Check if the problem is solved
        if self.__trucks[0].getCurrentWeight() != 0:
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
                    if truck.get_type() in box.getType().typeOfTruckToUse():
                        if truck.canContain(box):
                            truck.addFret(box)
                            boxes.remove(box)
                            __find_same_depot__(truck, boxes, box)

        #Check if all boxes are loaded in the trucks

        return self.__trucks