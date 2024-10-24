from ..utils import Box, Truck

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