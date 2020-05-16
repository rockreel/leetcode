import unittest

from l0332_reconstruct_itinerary import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
            Solution().findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]))
        self.assertEqual(
            ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
            Solution().findItinerary([['JFK', 'SFO'],['JFK', 'ATL'],['SFO', 'ATL'],['ATL', 'JFK'],['ATL', 'SFO']]))
        