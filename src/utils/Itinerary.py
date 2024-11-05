﻿
class Itinerary:
    """
    This class represents an itinerary, which is a sequence of waypoints that a vehicle must visit in order to reach its destination.
    """
    def __init__(self, start_location: int, end_location: int, waypoints: [int], travel_time: float):
        """
        This method initializes the itinerary.

        Args:
            start_location (int): The starting location of the itinerary.
            end_location (int): The ending location of the itinerary.
            waypoints ([int]): The waypoints that the vehicle must visit in order to reach its destination.
            travel_time (float): The time it takes to travel the itinerary.
        """
        if not isinstance(start_location, int) or not isinstance(end_location, int) or not isinstance(waypoints, list) or not (isinstance(travel_time, float)or isinstance(travel_time, int)):
            raise TypeError("Bad type of parameter")
        self.__start_location = start_location
        self.__end_location = end_location
        self.__waypoints = waypoints
        self.__travel_time = travel_time

    def getStartLocation(self) -> int:
        """
        This method returns the starting location of the itinerary.
        """
        return self.__start_location

    def getEndLocation(self) -> int:
        """
        This method returns the ending location of the itinerary.
        """
        return self.__end_location

    def getWaypoints(self) -> list:
        """
        This method returns the waypoints of the itinerary.
        """
        return list(self.__waypoints)

    def getTravelTime(self) -> float:
        """
        This method returns the time it takes to travel the itinerary.
        """
        return self.__travel_time

    def __eq__(self, other):
        """
        This method checks if two itineraries are equal.
        """
        if not isinstance(other, Itinerary):
            return False
        return self.__start_location == other.getStartLocation() and self.__end_location == other.getEndLocation() and self.__waypoints == other.getWaypoints() and self.__travel_time == other.getTravelTime()