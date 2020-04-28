import unittest

from l0248_strobogrammatic_number_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().strobogrammaticInRange('50', '100'))
