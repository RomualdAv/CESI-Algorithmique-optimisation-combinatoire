import sys
sys.path.insert(0, '../src')
import unittest
from utils.TypeBox import TypeBox

class TestTypeBox(unittest.TestCase):

    def test_should_place_alimental(self):
        listnotok = [TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
             TypeBox.OXIDIZING, TypeBox.PRESSURIZED]
        listok = [TypeBox.ALIMENTAL, TypeBox.NOTSPECIFY,TypeBox.FRAGILE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.ALIMENTAL,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.ALIMENTAL, listnotok))

    def test_should_place_notspecify(self):
        listnotok = []
        listok = [TypeBox.ALIMENTAL, TypeBox.NOTSPECIFY,TypeBox.FRAGILE,TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
             TypeBox.OXIDIZING, TypeBox.PRESSURIZED]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.NOTSPECIFY, listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.NOTSPECIFY, listnotok))

    def test_should_place_flammable(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
        TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY,TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.FLAMMABLE,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.FLAMMABLE, listnotok))

    def test_should_place_explosive(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
        TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY,TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.EXPLOSIVE,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.EXPLOSIVE, listnotok))

    def test_should_place_toxic(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,TypeBox.OXIDIZING]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.TOXIC,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.TOXIC, listnotok))

    def test_should_place_radioactive(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.CORROSIVE, TypeBox.OXIDIZING,
             TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY, TypeBox.TOXIC, TypeBox.RADIOACTIVE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.RADIOACTIVE,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.RADIOACTIVE, listnotok))

    def test_should_place_corrosive(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.OXIDIZING,
             TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY, TypeBox.TOXIC, TypeBox.CORROSIVE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.CORROSIVE,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.CORROSIVE, listnotok))

    def test_should_place_oxidizing(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
             TypeBox.PRESSURIZED, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY, TypeBox.TOXIC,TypeBox.OXIDIZING]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.OXIDIZING,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.OXIDIZING, listnotok))

    def test_should_place_pressurized(self):
        listnotok = [TypeBox.ALIMENTAL, TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
             TypeBox.OXIDIZING, TypeBox.FRAGILE]
        listok = [TypeBox.NOTSPECIFY, TypeBox.TOXIC, TypeBox.PRESSURIZED]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.PRESSURIZED,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.PRESSURIZED, listnotok))

    def test_should_place_fragile(self):
        listnotok = [TypeBox.FLAMMABLE, TypeBox.EXPLOSIVE, TypeBox.TOXIC, TypeBox.RADIOACTIVE, TypeBox.CORROSIVE,
             TypeBox.OXIDIZING, TypeBox.PRESSURIZED]
        listok = [TypeBox.NOTSPECIFY, TypeBox.ALIMENTAL, TypeBox.FRAGILE]

        self.assertTrue(TypeBox.isPossibleToTransport(TypeBox.FRAGILE,listok))
        self.assertFalse(TypeBox.isPossibleToTransport(TypeBox.FRAGILE, listnotok))

if __name__ == '__main__':
    unittest.main()