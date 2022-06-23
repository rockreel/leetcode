import unittest

from l0134_gas_station import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
        self.assertEqual(-1, Solution().canCompleteCircuit([2,3,4], [3,4,3]))
