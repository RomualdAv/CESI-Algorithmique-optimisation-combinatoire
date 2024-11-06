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

        self.boxes = boxes
        self.trucks = trucks
        self.graph = graph

    def sortByType(self) -> dict:
        """
        Sort the boxes by type.
        """
        order = dict()  
        for box in self.boxes:
            type_name = box.getType().name
            # Check if the type of the box is already in the dictionary
            if type_name not in order:
                order[type_name] = []
        
            # Add the box to the list of boxes of the same type
            order[type_name].append(box)
    
        return order
   

    def sortByTime (self, dict_boites: dict[str, list[Box]]) -> dict[str, list[Box]]:
        """
        Sort the boxes by delivery time.
        """
        for key, boites in dict_boites.items():
          
            boites.sort(key=lambda box: (box.getEnd(), -box.getDuration().total_seconds()))
            
        return dict_boites