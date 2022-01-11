import unittest

from l0841_keys_and_rooms import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().canVisitAllRooms([[1], [2], [3], []]))
        self.assertEqual(
            False, 
            Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
