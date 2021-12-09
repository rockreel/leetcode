import unittest

from l1299_replace_elements_with_greatest_element_on_right_side import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [18, 6, 6, 6, 1, -1], 
            Solution().replaceElements([17, 18, 5, 4, 6, 1]))
        self.assertEqual(
            [-1], 
            Solution().replaceElements([400]))

        