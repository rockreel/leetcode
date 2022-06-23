import unittest

from l0763_partition_labels import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([9,7,8], Solution().partitionLabels('ababcbacadefegdehijhklij'))
        self.assertEqual([10], Solution().partitionLabels('eccbbbbdec'))
