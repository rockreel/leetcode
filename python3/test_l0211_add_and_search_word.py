import unittest

from l0211_add_and_search_word import WordDictionary

class Test(unittest.TestCase):
    
    def test_solution(self):
        word_dict = WordDictionary()
        word_dict.addWord('bad')
        word_dict.addWord('dad')
        word_dict.addWord('mad')
        self.assertEqual(False, word_dict.search('pad'))
        self.assertEqual(True, word_dict.search('bad'))
        self.assertEqual(True, word_dict.search('.ad'))
        self.assertEqual(True, word_dict.search('b..'))

        word_dict = WordDictionary()
        word_dict.addWord('a')
        word_dict.addWord('a')
        self.assertEqual(True, word_dict.search('.'))
        self.assertEqual(True, word_dict.search('a'))
        self.assertEqual(False, word_dict.search('.a'))
        self.assertEqual(False, word_dict.search('a.'))