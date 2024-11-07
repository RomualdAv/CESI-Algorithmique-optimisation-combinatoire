from src.domains import InstanceError
from src.domains.SolutionChecker import is_solvable
from src.utils.Box import Box
from src.utils.Truck import Truck


class SortationAlgorithm:

    def __init__(self, boxes: list[Box], trucks: list[Truck], graph: list[list[float]]):
        """
        Constructeur de la classe SortationAlgorithm.

        :param boxes: List of boxes to deliver.
        :param trucks: List of trucks to deliver the boxes.
        :param graph: Graphe représentant les distances entre les points de livraison.

        :raises InstanceError: If the problem is not solvable.
        """

        is_solvable(trucks, boxes, graph)

        self.__boxes = boxes
        self.__trucks = trucks
        self.__graph = graph
        self.__dict_type = None
        self.__dict_type_sorted = None

        self.__dict_type = self.sortByType()
        self.checkContainability()

    def sortByType(self) -> dict:
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

    def checkContainability(self) -> bool:
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

    def sortByTime (self) -> dict[str, list[Box]]:
        """
        Sort the boxes by delivery time.
        """

        if self.__dict_type_sorted is not None:
            return self.__dict_type_sorted

        dict_copy = self.__dict_type.copy()

        for key, boites in dict_copy.items():

            boites.sort(key=lambda box: (box.getEnd(), -box.getDuration().total_seconds()))

        self.__dict_type_sorted = dict_copy

        return dict_copy