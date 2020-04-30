import unittest

import common
from l0251_flatten_2d_vector import Vector2D

class Test(unittest.TestCase):
    
    def test_solution(self):
        v = Vector2D([[1, 2], [3], [4, 5, 6]])
        self.assertEqual(True, v.hasNext())
        self.assertEqual(1, v.next())
        self.assertEqual(2, v.next())
        self.assertEqual(3, v.next())
        self.assertEqual(4, v.next())
        self.assertEqual(5, v.next())
        self.assertEqual(6, v.next())
        self.assertEqual(False, v.hasNext())
