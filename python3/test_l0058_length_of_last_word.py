import unittest

from l0058_length_of_last_word import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(5, Solution().lengthOfLastWord('Hello World'))
        self.assertEqual(5, Solution().lengthOfLastWord('Hello World  '))
