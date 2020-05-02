import unittest

from l0280_wiggle_sort import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = [3, 5, 2, 1, 6, 4]
        Solution().wiggleSort(l)
        self.assertTrue(l[0] <= l[1] and l[1] >= l[2] and l[2] <= l[3])
        self.assertTrue(l[3] >= l[4] and l[4] <= l[5])

        l = [1, 2, 3, 4]
        Solution().wiggleSort(l)
        self.assertTrue(l[0] <= l[1] and l[1] >= l[2] and l[2] <= l[3])
