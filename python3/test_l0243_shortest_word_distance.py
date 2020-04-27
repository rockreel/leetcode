import unittest

from l0243_shortest_word_distance import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'))
        self.assertEqual(1, Solution().shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'))
