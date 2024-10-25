from enum import Enum

"""
This class is an enumeration of the types of trucks.
"""
class TypeTruck(Enum):
    OPEN = 0
    REFRIGERATE = 1
    WATERTIGHT = 2
    PLATED = 3

    """
    This method returns the name of the type of truck.
    """
    def __str__(self):
        return self.name