import uuid

from src import CsvManager, Truck, Size, TypeTruck, Depot, Box, TypeBox


class InstanceLoader:
    """
    Class that loads an instance from a directory in a file with the instance_id as a suffix in the filename and provides methods to access the data
    """
    def __init__(self, directory: str, instance_id: str):
        if directory is None or instance_id is None or directory is not str or instance_id is not str:
            raise ValueError("directory and instance_id must be strings")
        self.directory = directory
        self.instance_id = instance_id
        self.graph_file = CsvManager(directory,"graph_"+instance_id+".csv")
        self.trucks_file = CsvManager(directory, "trucks_" + instance_id + ".csv")
        self.boxes_file = CsvManager(directory, "boxes_" + instance_id + ".csv")

    def get_trucks(self) -> list[Truck]:
        from src import CsvError
        """
        This method reads the trucks from the file and returns them as a list of Truck objects

        :return: list of Truck objects
        """
        trucks = []
        try:
            # Read all lines from the CSV file
            ligne_index = 0
            while True:
                # Reading a line at the current index
                ligne = self.trucks_file.readLine(ligne_index)
                if ligne_index == 0:
                    # Ignore the header
                    ligne_index += 1
                    continue
                else:
                    size = Size(ligne[1],float(ligne[2]),float(ligne[3]))
                    name = ligne[0]
                    match ligne[4]:
                        case "OPEN":
                            type_truck = TypeTruck.OPEN
                        case "REFRIGERATE":
                            type_truck = TypeTruck.REFRIGERATE
                        case "WATERTIGHT":
                            type_truck = TypeTruck.WATERTIGHT
                        case "PLATED":
                            type_truck = TypeTruck.PLATED
                        case _:
                            raise ValueError("Type de camion inconnu")
                    truck = Truck(name,size,type_truck)
                    trucks.append(truck)
                ligne_index += 1
        except CsvError:
            # When the end of the file is reached, the CsvError exception is raised
            return trucks

    def get_boxes(self) -> list[Box]:
        from src import CsvError
        """
        This method reads the boxes from the file and returns them as a list of Box objects

        :return: list of Box objects
        """
        boxes = []
        try:
            # Read all lines from the CSV file
            ligne_index = 0
            while True:
                # Reading a line at the current index
                ligne = self.boxes_file.readLine(ligne_index)
                if ligne_index == 0:
                    # Ignore the header
                    ligne_index += 1
                    continue
                else:
                    size = Size(ligne[3],float(ligne[4]),float(ligne[5]))
                    id_box = uuid.UUID(ligne[0])
                    depot = Depot(ligne[1],ligne[2])
                    match ligne[6]:
                        case "NOTSPECIFY":
                            type_box = TypeBox.NOTSPECIFY
                        case "ALIMENTAL":
                            type_box = TypeBox.ALIMENTAL
                        case "FLAMMABLE":
                            type_box = TypeBox.FLAMMABLE
                        case "EXPLOSIVE":
                            type_box = TypeBox.EXPLOSIVE
                        case "TOXIC":
                            type_box = TypeBox.TOXIC
                        case "RADIOACTIVE":
                            type_box = TypeBox.RADIOACTIVE
                        case "CORROSIVE":
                            type_box = TypeBox.CORROSIVE
                        case "OXIDIZING":
                            type_box = TypeBox.OXIDIZING
                        case "PRESSURIZED":
                            type_box = TypeBox.PRESSURIZED
                        case "FRAGILE":
                            type_box = TypeBox.FRAGILE
                        case _:
                            raise ValueError("Type de marchandise inconnu")
                    box = Box(id_box,depot,size,type_box)
                    boxes.append(box)
                ligne_index += 1
        except CsvError:
            # When the end of the file is reached, the CsvError exception is raised
            return boxes

    def get_graph(self) -> list[list[float]]:
        from src import CsvError
        """
        This method reads the trucks from the file and returns them as a list of Truck objects

        :return: list of Truck objects
        """
        graph = []
        try:
            # Read all lines from the CSV file
            ligne_index = 0
            while True:
                # Reading a line at the current index
                ligne = self.trucks_file.readLine(ligne_index)
                ligne_float = [float(i) for i in ligne]
                graph.append(ligne_float)
                ligne_index += 1
        except CsvError:
            # When the end of the file is reached, the CsvError exception is raised
            return graph