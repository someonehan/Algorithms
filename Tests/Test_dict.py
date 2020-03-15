import unittest
from src.DataStructure.Dict import UnsortedTableMap, ChainHashTableMap, ProbeHashTableMap


class Test_UnsortedTableMap(unittest.TestCase):
    def setUp(self):
        self.d = self._create_map()

    def test_add_one(self):
        self.d['name'] = "han"
        self.assertEqual(self.d['name'], "han")
        self.assertEqual(1, len(self.d))

    def test_add_two(self):
        self.d['name'] = "han"
        self.assertEqual(self.d['name'], "han")
        self.d['age'] = 23
        self.assertEqual(self.d['age'], 23)
        self.assertEqual(2, len(self.d))

    def test_del_one(self):
        self.d['name'] = "han"
        self.assertEqual(self.d['name'], "han")
        self.assertEqual(1, len(self.d))
        del self.d['name']
        self.assertEqual(0, len(self.d))

    def _create_map(self):
        return UnsortedTableMap()


class Test_ChainHashMap(Test_UnsortedTableMap):
    def _create_map(self):
        return ChainHashTableMap()


class Test_ProbeHashTableMap(Test_UnsortedTableMap):
    def _create_map(self):
        return ProbeHashTableMap()


if __name__ == "__main__":
    unittest.main()