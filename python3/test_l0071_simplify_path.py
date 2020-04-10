import unittest

from l0071_simplify_path import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('/home', Solution().simplifyPath('/home/'))
        self.assertEqual('/', Solution().simplifyPath('/../'))
        self.assertEqual('/home', Solution().simplifyPath('/home'))
        self.assertEqual('/home/foo', Solution().simplifyPath('/home//foo/'))