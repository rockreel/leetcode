import unittest

from l0739_daily_temperatures import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0], 
            Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
        self.assertEqual(
            [1, 1, 1, 0], 
            Solution().dailyTemperatures([30, 40, 50, 60]))
        self.assertEqual(
            [1, 1, 0], 
            Solution().dailyTemperatures([30, 60, 90]))
