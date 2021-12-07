import unittest

from l1295_find_numbers_with_even_number_of_digits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            2, 
            Solution().findNumbers([12, 345, 2, 6, 7896]))
        self.assertEqual(
            1, 
            Solution().findNumbers([555, 901, 482, 1771]))
        