import unittest

from l0787_cheapest_flights_within_k_stops import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(200, Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
        self.assertEqual(500, Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
