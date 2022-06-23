from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue