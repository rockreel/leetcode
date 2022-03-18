import unittest

from l0705_design_hashset import MyHashSet

class Test(unittest.TestCase):
    
    def test_solution(self):
        myhashset = MyHashSet()
        myhashset.add(1)
        myhashset.add(2)
        self.assertEqual(True, myhashset.contains(1))
        self.assertEqual(False, myhashset.contains(3))
        myhashset.add(2)
        self.assertEqual(True, myhashset.contains(2))
        myhashset.remove(2)
        self.assertEqual(False, myhashset.contains(2))