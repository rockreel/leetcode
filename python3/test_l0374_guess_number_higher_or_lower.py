import unittest

from l0374_guess_number_higher_or_lower import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution(6).guessNumber(10))
        self.assertEqual(1, Solution(1).guessNumber(1))
        self.assertEqual(1, Solution(1).guessNumber(2))
        self.assertEqual(2, Solution(2).guessNumber(2))
