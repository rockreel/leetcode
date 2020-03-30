import unittest

from l0038_count_and_say import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('1', Solution().countAndSay(1))
        self.assertEqual('11', Solution().countAndSay(2))
        self.assertEqual('21', Solution().countAndSay(3))
        self.assertEqual('1211', Solution().countAndSay(4))
        self.assertEqual('111221', Solution().countAndSay(5))