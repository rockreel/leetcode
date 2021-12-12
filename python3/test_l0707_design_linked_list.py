import unittest

from l0707_design_linked_list import MyLinkedList

class Test(unittest.TestCase):
    
    def test_solution(self):
        mylist = MyLinkedList()
        mylist.addAtHead(1)
        mylist.addAtTail(3)
        mylist.addAtIndex(1, 2)
        self.assertEqual(2, mylist.get(1))
        mylist.deleteAtIndex(0)
        self.assertEqual(2, mylist.get(0))