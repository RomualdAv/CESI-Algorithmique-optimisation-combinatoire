from ..utils import Box, Truck, Itinerary

def boxDeliveryWindowSorting(truck: Truck) -> list[Box]:
    """
    This function sorts the boxes in the truck by their delivery window.
    We used the deadline of the boxes to sort them in ascending order.

    Args:
        truck (Truck): The truck containing the boxes to be sorted
    """
    boxes = truck.get_fret()
    boxes = sorted(boxes, key=lambda x: x.getDestination().getDeliveryWindow().getEnd())
    return boxes

def createMatrixItinerary(graph: list[list[float]]) -> list[list[Itinerary]]:
    """
    This function creates a matrix of itinerary between the waypoints using the Floyd-Warshall algorithm.

    Args:
        graph (list[list[float]]): The graph containing the waypoints and the distances between them.
    """
    len_graph = len(graph)
    dist = [[Itinerary(i, j, [], graph[i][j]) for j in range(len_graph)] for i in range(len_graph)]

    for k in range(len_graph):
        for i in range(len_graph):
            for j in range(len_graph):
                # Update the distance by comparing direct distance and distance via k
                if dist[i][j].getTravelTime() > dist[i][k].getTravelTime() + dist[k][j].getTravelTime():
                    dist[i][j] = Itinerary(i, j, dist[i][k].getWaypoints() + [k] + dist[k][j].getWaypoints(), dist[i][k].getTravelTime() + dist[k][j].getTravelTime())

    return dist

def chainWaypointSorting(boxes: list[Box],distance: [],starting_depot: int) -> []:
    """
    This function search the shortest path between the boxes using the graph.

    Args:
        boxes (list[Box]): The boxes to be sorted
        distance ([]): The matrix of distances between the waypoints
        starting_depot (int): The starting depot
    """
    ways = []
    index = 0
    now_point = starting_depot
    while len(ways) < len(boxes):
        next_point = boxes[index].getDestination().getLocation()
        ways.append(distance[now_point][next_point])
    return ways