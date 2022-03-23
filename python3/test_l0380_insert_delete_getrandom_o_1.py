import unittest

from l0380_insert_delete_getrandom_o_1 import RandomizedSet

class Test(unittest.TestCase):
    
    def test_solution(self):
        r = RandomizedSet()        
        self.assertEqual(True, r.insert(1))
        self.assertEqual(False, r.remove(2))
        self.assertEqual(True, r.insert(2))
        self.assertEqual(True, r.remove(1))
        self.assertEqual(False, r.insert(2))
