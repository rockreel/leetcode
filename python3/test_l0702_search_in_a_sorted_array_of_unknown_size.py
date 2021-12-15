import unittest

from l0702_search_in_a_sorted_array_of_unknown_size import ArrayReader
from l0702_search_in_a_sorted_array_of_unknown_size import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        reader = ArrayReader([-1,0,3,5,9,12])
        self.assertEqual(4, Solution().search(reader, 9))
        self.assertEqual(-1, Solution().search(reader, 2))

