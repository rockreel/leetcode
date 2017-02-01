class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import bisect
        ups = [[l, -1, -h] for l, _, h in buildings]
        downs = [[r, 1, h] for _, r, h in buildings]
        # Sort by position, up or down, then height.
        # If up edge, put higher height (negative height) first to avoid dedup later.
        edges = sorted(ups + downs)
        heights = []  # Sorted existing heights, heights[-1] is the max so far.
        skylines = []
        for i, t, h in edges:
            if t == -1:  # Up edge.
                h = -h
                if not heights or h > heights[-1]:
                    skylines.append([i, h])
                bisect.insort_left(heights, h)
            else:  # Down edge.
                heights.pop(bisect.bisect_left(heights, h))
                if not heights:
                    skylines.append([i, 0])
                elif heights[-1] < h:
                    skylines.append([i, heights[-1]])
                    
        return skylines

