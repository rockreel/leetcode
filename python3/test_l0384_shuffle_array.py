import unittest

from l0384_shuffle_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        s = Solution([1, 2, 3])        
        self.assertEqual([1, 2, 3], s.reset())
        self.assertEqual(3, len(s.shuffle()))
        self.assertEqual(3, len(s.shuffle()))
        self.assertEqual(3, len(s.shuffle()))
        