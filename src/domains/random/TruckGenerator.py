import random
import uuid
import datetime

from src import Truck
from src import Box
from src import TypeTruck
from src import Size
from src import TypeBox
from src import Depot
from src import DeliveryWindow


def generate_truck(nb_truck: int) -> list[Truck]:
    """
    Generate a list of truck with random values
    :param nb_truck: Number of truck to generate
    :return: A list of truck
    """
    truck_list = list()
    index = 1
    for _ in range(nb_truck):
        name = f"Truck_{index}"
        index += 1
        size = Size(random.randint(10, 100), random.randint(10, 100), random.randint(10, 100))
        truck_type = random.choice([TypeTruck.OPEN, TypeTruck.WATERTIGHT,TypeTruck.REFRIGERATE,TypeTruck.PLATED])
        truck = Truck(name, size, truck_type)
        truck_list.append(truck)

    return truck_list

def generate_box(truck: Truck,nb_nodes: int,start_node: int) -> None:
    """
    Generate a random number of box for a truck
    :param truck: The truck to fill
    :param nb_nodes: The number of nodes in the graph
    :param start_node: The start node of the truck
    """
    coef_max_width = truck.get_size().get_width()//10
    coef_min_width = truck.get_size().get_width()//30
    coef_max_height = truck.get_size().get_height() // 10
    coef_min_height = truck.get_size().get_height() // 30
    coef_max_length = truck.get_size().get_length() // 10
    coef_min_length = truck.get_size().get_length() // 30
    for _ in range(random.randint(1, 25)):
        # Generate a random Depot
        node = random.randint(0, nb_nodes-1)
        while node == start_node:
            node = random.randint(0, nb_nodes-1)

        date1 = datetime.datetime(2024, 1, 1, random.randint(0, 12), random.choice([0, 30]))
        date2 = datetime.datetime(2024, 1, 1, random.randint(12, 23), random.choice([31, 59]))
        depot = Depot(node, f"Depot_{node}", random.choice([True, False]), DeliveryWindow(date1, date2))
        # Generate a random box
        id = uuid.uuid4()
        size = Size(random.randint(coef_min_width, coef_max_width), random.randint(coef_min_height, coef_max_height), random.randint(coef_min_length, coef_max_length))
        if truck.get_size().getVolume() < truck.getCurrentWeight()+size.getVolume():
            whp = truck.get_size().getVolume() - truck.getCurrentWeight()//3
            # Check if the box is less or equal to 4% of the truck size volume for stop iteration
            if whp <= (truck.get_size().getVolume()/100)*4:
                break
            size = Size(whp, whp, whp)

        match truck.get_type():
            case TypeTruck.OPEN:
                box_type = random.choice([TypeBox.NOTSPECIFY,TypeBox.FLAMMABLE,TypeBox.EXPLOSIVE,TypeBox.PRESSURIZED,TypeBox.FRAGILE])
            case TypeTruck.WATERTIGHT:
                box_type = random.choice([TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.CORROSIVE, TypeBox.OXIDIZING,TypeBox.FRAGILE])
            case TypeTruck.REFRIGERATE:
                box_type = random.choice([TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL,TypeBox.FRAGILE])
            case TypeTruck.PLATED:
                box_type = random.choice([TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING, TypeBox.PRESSURIZED,TypeBox.FRAGILE])
            case _:
                box_type = TypeBox.NOTSPECIFY
        box = Box(id,depot ,size, box_type)
        truck.addFret(box)

        # Check if the truck is full
        if truck.isFull():
            break