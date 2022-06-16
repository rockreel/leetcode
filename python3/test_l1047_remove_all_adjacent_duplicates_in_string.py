import unittest

from l1047_remove_all_adjacent_duplicates_in_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('ca', Solution().removeDuplicates('abbaca'))
        self.assertEqual('ay', Solution().removeDuplicates('azxxzy'))
