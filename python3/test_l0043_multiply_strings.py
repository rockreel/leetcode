import unittest

from l0043_multiply_strings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('6', Solution().multiply('2', '3'))
        self.assertEqual('56088', Solution().multiply('123', '456'))
        self.assertEqual('0', Solution().multiply('123', '0'))

