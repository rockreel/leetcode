import random

class RandomizedSet:

    def __init__(self):
        self._nums = []
        self._position_map = {}
        
    def insert(self, val: int) -> bool:
        if val not in self._position_map:
            self._position_map[val] = len(self._nums)
            self._nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self._position_map:
            i = self._position_map[val]
            self._nums[i] = self._nums[-1]
            self._position_map[self._nums[-1]] = i
            self._nums.pop()
            self._position_map.pop(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self._nums)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()