import unittest
import uuid
import datetime
import sys
import uuid
sys.path.insert(0, '../src')
import unittest
from domains.Load import Load
from utils.Box import Box
from utils.Size import Size
from utils.Depot import Depot
from utils.Truck import Truck
from utils.TypeBox import TypeBox
from utils.DeliveryWindow import DeliveryWindow

class TestChargement(unittest.TestCase):

    def setUp(self):
        """Configuration de base pour chaque test."""
        self.truck = Truck(max_weight=1000, max_volume=5000)
        self.chargement = Load(self.truck)

        # Création de quelques boîtes pour les tests
        self.box1 = Box(id=uuid.uuid4(), weight=200, volume=1000, box_type='fragile', delivery_time=30, priority=2)
        self.box2 = Box(id=uuid.uuid4(), weight=300, volume=1500, box_type='normal',delivery_time=10, priority= 4)
        self.box3 = Box(id=uuid.uuid4(), weight=150, volume=500, box_type='fragile', delivery_time=20,priority=1)
        self.box4 = Box(id=uuid.uuid4(), weight=400, volume=1200, box_type='normal', delivery_time=40,priority= 3)

        # création de quelques camions pour les tests
        self.trucks = [Truck(capacity=2), Truck(capacity=1)]

    def test_should_load_box_when_capacity_is_available(self):
        """Vérifie si une boîte peut être chargée lorsque la capacité est disponible."""
        self.chargement.load_box(self.box1)
        self.assertIn(self.box1, self.chargement.loaded_boxes)
        self.assertEqual(self.chargement.total_weight, self.box1.weight)
        self.assertEqual(self.chargement.total_volume, self.box1.volume)


    def test_should_not_load_box_when_capacity_is_exceeded(self):
        """Vérifie que la boîte n'est pas chargée si la capacité est dépassée."""
        self.chargement.load_box(self.box2)  # Charge box2
        self.chargement.load_box(self.box4)  # Charge box4
        self.assertNotIn(self.box3, self.chargement.loaded_boxes) # Assure que box3 ne peut pas être chargée

    def test_should_load_multiple_boxes(self):
        """Teste le chargement de plusieurs boîtes à la fois."""
        self.chargement.load_boxes([self.box1, self.box2, self.box3])
        self.assertIn(self.box1, self.chargement.loaded_boxes)
        self.assertIn(self.box2, self.chargement.loaded_boxes)
        self.assertIn(self.box3, self.chargement.loaded_boxes)
        self.assertEqual(self.chargement.total_weight, self.box1.weight + self.box2.weight + self.box3.weight)
        self.assertEqual(self.chargement.total_volume, self.box1.volume + self.box2.volume + self.box3.volume)

    def test_should_return_remaining_capacity(self):
        """Test la capacité restante après le chargement de boîtes."""
        self.chargement.load_boxes([self.box1, self.box2])
        remaining_weight, remaining_volume = self.chargement.remaining_capacity()
        self.assertEqual(remaining_weight, self.truck.max_weight - (self.box1.weight + self.box2.weight))
        self.assertEqual(remaining_volume, self.truck.max_volume - (self.box1.volume + self.box2.volume))


    def test_load_trucks_by_time(self):
        """Teste le chargement des camions selon le temps de livraison."""
        self.load.load_trucks_by_time(self.trucks)

        # Vérification des colis chargés dans le premier camion
        self.assertEqual(len(self.trucks[0].loaded_boxes), 2)
        self.assertEqual(self.trucks[0].loaded_boxes[0].delivery_time, 10)  # box2
        self.assertEqual(self.trucks[0].loaded_boxes[1].delivery_time, 20)  # box3

        # Vérification des colis chargés dans le deuxième camion
        self.assertEqual(len(self.trucks[1].loaded_boxes), 1)
        self.assertEqual(self.trucks[1].loaded_boxes[0].delivery_time, 30)  # box1

    def test_load_box_success(self): ##
        """Test de chargement d'une boîte avec succès."""
        self.setup()
        self.load_manager.load_boxes(self.truck1, [self.box1, self.box2])
        assert self.truck1.getCurrentWeight() == 500, "Test Failed: Truck weight should be 500"
        assert len(self.load_manager.truck_graph[self.truck1.get_name()]) == 2, "Test Failed: Two boxes should be loaded"
        print("test_load_box_success passed.")

    def test_should_unload_box(self):
        """Teste la décharge d'une boîte."""
        self.chargement.load_box(self.box1)
        self.chargement.unload_box(self.box1.id)
        self.assertNotIn(self.box1, self.chargement.loaded_boxes)
        self.assertEqual(self.chargement.total_weight, 0)
        self.assertEqual(self.chargement.total_volume, 0)
        
    def test_should_not_unload_non_existent_box(self):

        """Teste le comportement lorsqu'on essaie de décharger une boîte qui n'existe pas."""
        self.chargement.load_box(self.box1)
        initial_length = len(self.chargement.loaded_boxes)
        self.chargement.unload_box(uuid.uuid4())  # ID d'une boîte qui n'existe pas
        self.assertEqual(len(self.chargement.loaded_boxes), initial_length)  # La longueur ne doit pas changer

if __name__ == '__main__':
    unittest.main()