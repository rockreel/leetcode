import unittest

from l0983_minimum_cost_for_tickets import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            11, 
            Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]))
        self.assertEqual(
            17, 
            Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
