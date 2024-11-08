"""
This class represents a depot. A depot is a place where the vehicle can park and deliver the goods.

Attributes:
    - location (Vertex): Vertex on the graph
    - name (string): Name of the depot
"""
class Depot:

    def __init__(self, location: int, name : str):
        if not isinstance(location, int) or not isinstance(name, str):
            raise AttributeError("Attribut type is not correct")
        self.__location = location
        self.__name= name

    def getLocation(self) -> int:
        """
        This method returns the location of the depot.
        """
        return self.__location

    def getName(self) -> str:
        """
        This method returns the name of the depot.
        """
        return self.__name

    def __str__(self) -> str:
        return f"Depot : {self.__name}, Location: {self.__location}"
    
       