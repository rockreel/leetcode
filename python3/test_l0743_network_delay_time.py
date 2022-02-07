import unittest

from l0743_network_delay_time import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
        self.assertEqual(1, Solution().networkDelayTime([[1,2,1]], 2, 1))
        self.assertEqual(-1, Solution().networkDelayTime([[1,2,1]], 2, 2))
