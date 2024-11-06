﻿from src.domains.generator.GraphGenerator import *
from src.domains.generator.TruckGenerator import *
from src.infrastructure.CSVManager import *
from error import InstanceError


def generate_instance(directory: str, nb_nodes: int, nb_edges: int, symmetric: bool, nb_truck: int):
    """
    Generate an instance with generator values
    :param directory: The directory where the instance will be saved
    :param nb_nodes: The number of nodes in the graph
    :param nb_edges: The number of edges in the graph
    :param symmetric: If the graph is symmetric
    :param nb_truck: The number of truck in the instance
    """
    # Generate the graph
    graph = generateGraph(nb_nodes, nb_edges, symmetric)
    # Generate the trucks
    trucks = generate_truck(nb_truck)
    for truck in trucks:
        starting_node = random.randint(0, nb_nodes - 1)
        generate_box(truck, nb_nodes, starting_node)
    # Generate an id for the instance
    instance_id = str(uuid.uuid4())
    instance_id = instance_id[0:8]
    try:
        # Save the instance
        # Save the graph
        graph_file = CsvManager(directory, "graph_" + instance_id + ".csv", graph)
        # Save the trucks
        header = [["Name", "Width", "Height", "Length", "Type"]]
        truck_file = CsvManager(directory, "trucks_" + instance_id, header)
        for truck in trucks:
            truck_file.addLine([truck.get_name(),
                                      truck.get_size().get_width(),
                                      truck.get_size().get_height(),
                                      truck.get_size().get_length(),
                                      truck.get_type().name])
        # Save the box
        header = [
            ["Id", "Location_Depot", "Name_Depot", "Parking_Depot", "Start_Delivery_Window", "End_Delivery_Window", "Width",
             "Height", "Length", "Type"]]
        box_file = CsvManager(directory, "boxes_" + instance_id, header)
        for truck in trucks:
            for box in truck.get_fret():
                box_file.addLine([box.getIdBox(),
                                        box.getDestination().getLocation(),
                                        box.getDestination().getName(),
                                        box.getDestination().getPossibilityParking(),
                                        box.getDestination().getDeliveryWindow().getStart(),
                                        box.getDestination().getDeliveryWindow().getEnd(),
                                        box.getSize().get_width(),
                                        box.getSize().get_height(),
                                        box.getSize().get_length(),
                                        box.getType().name])
    except CsvError as e:
        raise InstanceError(f"Error while saving the instance: {e}")

generate_instance("../infrastructure/instances", 10, 20, True, 2)
