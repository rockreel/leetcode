import unittest

from l0244_shortest_word_distance_2 import WordDistance

class Test(unittest.TestCase):
    
    def test_solution(self):
        wd = WordDistance(['practice', 'makes', 'perfect', 'coding', 'makes'])
        self.assertEqual(3, wd.shortest('coding', 'practice'))
        self.assertEqual(1, wd.shortest('makes', 'coding'))
