from collections import defaultdict

"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        sea = [[0] * m for _ in range(n)]
        marker_to_island_map = dict()
        island_to_marker_map = defaultdict(list)
        marker = 1
        num_islands = []
        for op in operators:
            connected_islands = set()
            if sea[op.x][op.y] != 0:
                connected_islands.add(marker_to_island_map[sea[op.x][op.y]])
            if op.x - 1 >= 0 and sea[op.x-1][op.y] != 0:
                connected_islands.add(marker_to_island_map[sea[op.x-1][op.y]])
            if op.x + 1 < n and sea[op.x+1][op.y] != 0:
                connected_islands.add(marker_to_island_map[sea[op.x+1][op.y]])
            if op.y - 1 >= 0 and sea[op.x][op.y-1] != 0:
                connected_islands.add(marker_to_island_map[sea[op.x][op.y-1]])
            if op.y + 1 < m and sea[op.x][op.y+1] != 0:
                connected_islands.add(marker_to_island_map[sea[op.x][op.y+1]])
            if len(connected_islands) == 0:
                # Not connect to any islands.
                sea[op.x][op.y] = marker
                marker_to_island_map[marker] = marker
                island_to_marker_map[marker].append(marker)
                marker += 1
            elif len(connected_islands) == 1:
                # Connect only to one island.
                island = connected_islands.pop()
                sea[op.x][op.y] = island_to_marker_map[island][0]
            else:
                # Connect to more than one island.
                merge_to_island = connected_islands.pop()
                for island in connected_islands:
                    for mk in island_to_marker_map[island]:
                        marker_to_island_map[mk] = merge_to_island
                        island_to_marker_map[merge_to_island].append(mk)
                    island_to_marker_map.pop(island)
                sea[op.x][op.y] = island_to_marker_map[merge_to_island][0]
            num_islands.append(len(island_to_marker_map.keys()))
        return num_islands