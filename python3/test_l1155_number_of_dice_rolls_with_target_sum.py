import unittest

from l1155_number_of_dice_rolls_with_target_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1, 
            Solution().numRollsToTarget(1, 6, 3))
        self.assertEqual(
            6, 
            Solution().numRollsToTarget(2, 6, 7))
        self.assertEqual(
            222616187, 
            Solution().numRollsToTarget(30, 30, 500))

