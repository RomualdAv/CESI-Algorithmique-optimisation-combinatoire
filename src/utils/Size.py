
"""Use this class for the size of any object in 3D space"""
class Size:
    """
    Constructor of the class Size.

    width: the width of the size
    height: the height of the size
    length: the length of the size

    Raise a ValueError if the width, height or length is negative
    """
    def __init__(self, width:float, height:float, length:float):
        if width < 0 or height < 0 or length < 0:
            raise ValueError("Width, height and length must be positive")
        self.__width = width
        self.__height = height
        self.__length = length

    def get_width(self):
        """
        Method to get the width of the size
        """
        return self.__width
    def get_height(self):
        """
        Method to get the height of the size
        """
        return self.__height
    def get_length(self):
        """
        Method to get the length of the size
        """
        return self.__length
    """Method to get the volume of the size"""
    def getVolume(self):
        return self.__width * self.__height * self.__length
    """Method to get the width of the size"""
    def __str__(self):
        return f"(width :{self.__width}, height :{self.__height}, length :{self.__length})"