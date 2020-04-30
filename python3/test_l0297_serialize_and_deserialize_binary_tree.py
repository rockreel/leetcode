import unittest

import common
from l0297_serialize_and_deserialize_binary_tree import Codec

class Test(unittest.TestCase):
    
    def test_solution(self):
        codec = Codec()
        root = common.create_binary_tree([1, 2, 3, None, None, 4, 5])
        self.assertEqual(
            [1, 2, 3, None, None, 4, 5],
            common.convert_binary_tree_to_list(codec.deserialize(codec.serialize(root))))
