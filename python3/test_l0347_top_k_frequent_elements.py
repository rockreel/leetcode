import unittest

from l0347_top_k_frequent_elements import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 2], Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
        self.assertEqual([1], Solution().topKFrequent([1], 1))