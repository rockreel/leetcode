class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        # Write your code here
        def cal_dist(points):
            points.sort()
            i, j = 0, len(points) - 1
            dist = 0
            while i < j:
                dist += points[j] - points[i]
                i += 1
                j -= 1
            return dist
                     
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        return cal_dist(rows) + cal_dist(cols)
