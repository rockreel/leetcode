import unittest

from l0245_shortest_word_distance_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'))
        self.assertEqual(3, Solution().shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes'))
        self.assertEqual(3, Solution().shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'))