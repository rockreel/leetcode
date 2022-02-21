import unittest

from l0677_map_sum_pairs import MapSum

class Test(unittest.TestCase):
    
    def test_solution(self):
        m = MapSum()
        m.insert('apple', 3)
        self.assertEqual(3, m.sum('ap'))
        m.insert('app', 2)
        self.assertEqual(5, m.sum('ap'))
