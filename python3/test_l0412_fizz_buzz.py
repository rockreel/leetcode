import unittest

from l0412_fizz_buzz import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['1','2','Fizz'], Solution().fizzBuzz(3))
        self.assertEqual(['1','2','Fizz','4','Buzz'], Solution().fizzBuzz(5))
        self.assertEqual(['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz'], Solution().fizzBuzz(15))

