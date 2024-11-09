import unittest
from src.domains.generator.TruckGenerator import generate_truck, generate_box
from src import Truck, Size, TypeTruck, TypeBox


class TestTruckGenerator(unittest.TestCase):

    def test_generate_the_good_number_of_truck(self):
        nb_truck = 5
        trucks = generate_truck(nb_truck)

        self.assertEqual(len(trucks), nb_truck)
        for truck in trucks:
            self.assertIsInstance(truck, Truck)
            self.assertIn(truck.get_type(),[TypeTruck.OPEN, TypeTruck.WATERTIGHT, TypeTruck.REFRIGERATE, TypeTruck.PLATED])

    def test_check_type_truck_and_type_box(self):
        nb_truck = 10
        trucks = generate_truck(nb_truck)

        self.assertEqual(len(trucks), nb_truck)
        for truck in trucks:
            self.assertIsInstance(truck, Truck)
            for box in truck.get_fret():
                match truck.get_type():
                    case TypeTruck.OPEN:
                        self.assertIn(box.get_type(),[TypeBox.NOTSPECIFY,TypeBox.FLAMMABLE,TypeBox.EXPLOSIVE,TypeBox.PRESSURIZED,TypeBox.FRAGILE])
                    case TypeTruck.WATERTIGHT:
                        self.assertIn(box.get_type(),[TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.CORROSIVE, TypeBox.OXIDIZING,TypeBox.FRAGILE])
                    case TypeTruck.REFRIGERATE:
                        self.assertIn(box.get_type(),[TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL,TypeBox.FRAGILE])
                    case TypeTruck.PLATED:
                        self.assertIn(box.get_type(),[TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING, TypeBox.PRESSURIZED,TypeBox.FRAGILE])
                    case _:
                        self.fail("Type not found")

    def test_check_fret(self):
        truck = Truck("Test_Truck", Size(50, 50, 50), TypeTruck.OPEN)
        nb_nodes = 10
        start_node = 0
        generate_box(truck, nb_nodes, start_node)

        self.assertGreater(len(truck.get_fret()), 0)
        self.assertLessEqual(len(truck.get_fret()), 25)
        self.assertLessEqual(truck.get_current_weight(), truck.get_size().getVolume())
        for box in truck.get_fret():
            self.assertNotEqual(box.get_destination().get_location(), start_node)


if __name__ == '__main__':
    unittest.main()