import unittest

from l0648_replace_words import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('the cat was rat by the bat', Solution().replaceWords(['cat','bat','rat'], 'the cattle was rattled by the battery'))
        self.assertEqual('a a b c', Solution().replaceWords(['a','b','c'], 'aadsfasf absbs bbab cadsfafs'))
