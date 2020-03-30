import unittest

from l0038_count_and_say import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('1211', Solution().countAndSay(4))