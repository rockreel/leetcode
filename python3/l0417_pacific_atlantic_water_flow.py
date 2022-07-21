from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def find_can_flow_blocks(heights, seed_blocks):
            visited = set([])
            flow_blocks = set([])
            queue = [s for s in seed_blocks]
            while queue:
                r, c = queue.pop(0)
                visited.add((r, c))
                flow_blocks.add((r, c))
                if r > 0 and (r-1, c) not in visited and heights[r-1][c] >= heights[r][c]:
                    queue.append((r-1, c))
                if r < len(heights) - 1 and (r+1, c) not in visited and heights[r+1][c] >= heights[r][c]:
                    queue.append((r+1, c))
                if c > 0 and (r, c-1) not in visited and heights[r][c-1] >= heights[r][c]:
                    queue.append((r, c-1))
                if c < len(heights[0]) - 1 and (r, c+1) not in visited and heights[r][c+1] >= heights[r][c]:
                    queue.append((r, c+1))
            return flow_blocks
            
        seed_pacific = []
        seed_pacific.extend([(i, 0) for i in range(len(heights))])
        seed_pacific.extend([(0, j) for j in range(len(heights[0]))])
        pacific = find_can_flow_blocks(heights, seed_pacific)
        
        seed_atlantic = []
        seed_atlantic.extend([(i, len(heights[0])-1) for i in range(len(heights))])
        seed_atlantic.extend([(len(heights)-1, j) for j in range(len(heights[0]))])
        atlantic = find_can_flow_blocks(heights, seed_atlantic)
        
        result = pacific.intersection(atlantic)
        return [[r[0], r[1]] for r in result]