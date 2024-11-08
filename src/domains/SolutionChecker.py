from src.domains import InstanceError
from src.utils.Box import Box
from src.utils.Truck import Truck

def is_solvable(camions: list[Truck], boites: list[Box], graph: list[list[float]]) -> bool:
    """
    This function checks if the boxes can be delivered by the trucks

    :param camions: list of trucks
    :param boites: list of boxes
    :param graph: graph representing a map

    :raises InstanceError: if the total volume of the boxes is greater than the total volume of the trucks
    :raises InstanceError: if the destination of the boxes is unreachable by the trucks

    :return: True if the boxes can be delivered by the trucks
    """
    # Check if there are trucks and boxes
    if not camions:
        raise InstanceError("Aucun camion")

    elif not boites:
        raise InstanceError("Aucune boite")

    elif not graph:
        raise InstanceError("Aucun graphe")

    # Check if the total volume of the boxes is less than the total volume of the trucks
    elif not is_containable(boites, camions):
        raise InstanceError("Volume total des boites supérieur au volume total des camions")

    # Check if the destination of the boxes is reachable by the trucks
    elif not is_reachable(boites, graph):
        raise InstanceError("Destination des boites non atteignable par les camions")

    return True

def is_reachable(boites: list[Box], graph: list[list[float]]) -> bool:
    """
    This function checks if the destination of the boxes is reachable by the trucks

    :param boites: list of boxes
    :param graph: graph representing a map
    """
    for box in boites:
        if box.getDestination().getLocation() not in range(len(graph)):
            return False

    return True
    
def is_containable(boxs: list[Box], trucks: list[Truck]) -> bool:
    """
    This function checks if the total volume of the boxes is less than the total volume of the trucks
    """
    volume_total_boites = sum(box.getSize().getVolume() for box in boxs)
    volume_total_truck = sum(truck.get_size().getVolume() for truck in trucks)

    if volume_total_boites > volume_total_truck:
        return False

    return True