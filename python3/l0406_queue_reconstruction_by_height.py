from typing import List
from collections import deque

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        queue = deque()
        for p in people:
            queue.insert(p[1], p)
        return queue