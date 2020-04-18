import unittest

import common
from l0146_lru_cache import LRUCache

class Test(unittest.TestCase):
    
    def test_solution(self):
        # cache = LRUCache(2)
        # cache.put(1, 1)
        # cache.put(2, 2)
        # self.assertEqual(1, cache.get(1))
        # cache.put(3, 3)
        # self.assertEqual(-1, cache.get(2))
        # cache.put(4, 4)
        # self.assertEqual(-1, cache.get(1))
        # self.assertEqual(3, cache.get(3))
        # self.assertEqual(4, cache.get(4))

        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(1, 2)
        cache.put(2, 3)
        cache.put(4, 1)
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(2))