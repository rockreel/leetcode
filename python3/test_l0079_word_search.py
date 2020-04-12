import unittest

from l0079_word_search import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertEqual(True, Solution().exist(board, 'ABCCED'))
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertEqual(True, Solution().exist(board, 'SEE'))
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertEqual(False, Solution().exist(board, 'ABCB'))
        board = [
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a']
        ]
        self.assertEqual(False, Solution().exist(board, 'aaaaaaaaaaaaa'))
