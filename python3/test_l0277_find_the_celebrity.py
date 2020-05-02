import unittest

from l0277_find_the_celebrity import Celebrity
from l0277_find_the_celebrity import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        Celebrity.knows_graph = set([
            (0, 1),
        ])
        self.assertEqual(1, Solution().findCelebrity(2))

        Celebrity.knows_graph = set([
            (1, 0), (2, 0), (2, 1)
        ])
        self.assertEqual(0, Solution().findCelebrity(2))

        Celebrity.knows_graph = set([
            (0, 3), (0, 5), (1, 2), (2, 0), (2, 1), (2, 5),
            (3, 0), (3, 1), (3, 5), (4, 1),
            (5, 0), (5, 1), (5, 2)
        ])
        self.assertEqual(-1, Solution().findCelebrity(6))
        