import unittest

from l0599_minimum_index_sum_of_two_lists import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            ["Shogun"], 
            Solution().findRestaurant(
                ["Shogun","Tapioca Express","Burger King","KFC"], 
                ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
            ))
        self.assertEqual(
            ["Shogun"], 
            Solution().findRestaurant(
                ["Shogun","Tapioca Express","Burger King","KFC"],
                ["KFC","Shogun","Burger King"]
            ))
        