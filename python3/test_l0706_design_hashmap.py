import unittest

from l0706_design_hashmap import MyHashMap

class Test(unittest.TestCase):
    
    def test_solution(self):
        myhashmap = MyHashMap()
        myhashmap.put(1, 1)
        myhashmap.put(2, 2)
        self.assertEqual(1, myhashmap.get(1))
        self.assertEqual(-1, myhashmap.get(3))
        myhashmap.put(2, 1)
        self.assertEqual(1, myhashmap.get(2))
        myhashmap.remove(2)
        self.assertEqual(-1, myhashmap.get(2))