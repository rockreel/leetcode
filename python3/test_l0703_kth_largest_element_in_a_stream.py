import unittest
from l0703_kth_largest_element_in_a_stream import KthLargest

class Test(unittest.TestCase):
    
    def test_solution(self):
        kth = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(4, kth.add(3))
        self.assertEqual(5, kth.add(5))
        self.assertEqual(5, kth.add(10))
        self.assertEqual(8, kth.add(9))
        self.assertEqual(8, kth.add(4))
