import datetime

"""
Method to copy the datetime object
"""
def copyDatetime(date):
    return datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)

"""
This class represents the delivery window with a start and end datetime.
"""
class DeliveryWindow:
    def __init__(self, start, end):
        if not isinstance(start, datetime.datetime):
            raise ValueError("Start should be a datetime object")
        if not isinstance(end, datetime.datetime):
            raise ValueError("End should be a datetime object")
        self.__start = copyDatetime(start)
        self.__end = copyDatetime(end)
    """
    Method to get the start time of the delivery window
    """
    def getStart(self):
        return copyDatetime(self.__start)
    """
    Method to get the end time of the delivery window
    """
    def getEnd(self):
        return copyDatetime(self.__end)
    """
    Method to get the duration of the delivery window
    """
    def getDuration(self):
        return self.__end - self.__start

    def __str__(self):
        return f"{self.__start.year}-{self.__start.month}-{self.__start.day} {self.__start.hour}:{self.__start.minute} | {self.__end.year}-{self.__end.month}-{self.__end.day} {self.__end.hour}:{self.__end.minute}"