from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = set([])
        while queue:
            r = queue.pop()
            visited.add(r)
            for k in rooms[r]:
                if k not in visited:
                    queue.append(k)
        return len(visited) == len(rooms)