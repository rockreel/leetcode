from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        fruit_picked_map = {}
        num_fruit_picked = 0
        max_num_fruit_picked = 0
        
        while end < len(fruits):
            while len(fruit_picked_map) <= 2 and end < len(fruits):
                max_num_fruit_picked = max(num_fruit_picked, max_num_fruit_picked)
                if fruits[end] not in fruit_picked_map:
                    fruit_picked_map[fruits[end]] = 1
                else:
                    fruit_picked_map[fruits[end]] += 1
                num_fruit_picked += 1
                end += 1

            while len(fruit_picked_map) > 2:
                fruit_picked_map[fruits[start]] -= 1
                num_fruit_picked -= 1
                if fruit_picked_map[fruits[start]] == 0:
                    fruit_picked_map.pop(fruits[start])
                start += 1
            max_num_fruit_picked = max(num_fruit_picked, max_num_fruit_picked)
                
        return max_num_fruit_picked