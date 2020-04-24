import unittest

from l0208_implement_trie import Trie

class Test(unittest.TestCase):
    
    def test_solution(self):
        trie = Trie()
        trie.insert('apple')
        self.assertEqual(True, trie.search('apple'))
        self.assertEqual(False, trie.search('app'))
        self.assertEqual(True, trie.startsWith('app'))
        trie.insert('app')
        self.assertEqual(True, trie.search('app'))