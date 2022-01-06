import unittest

from l0752_open_the_lock import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().openLock(["0201", "0101", "0102", "1212", "2002"], '0202'))
        self.assertEqual(1, Solution().openLock(["8888"], '0009'))
        self.assertEqual(-1, Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888'))
