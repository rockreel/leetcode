class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        
        def update_dist(rooms, row, col):
            queue = [((row, col), 0)]
            visited = set([(row, col)])
            while queue:
                (i, j), d = queue.pop(0)
                rooms[i][j] = min(rooms[i][j], d)
                if (i - 1 >= 0 and rooms[i-1][j] not in (0, -1) and
                    (i-1, j) not in visited):
                    queue.append(((i-1, j), d+1))
                    visited.add((i-1, j))
                if (i + 1 < len(rooms) and rooms[i+1][j] not in (0, -1) and 
                      (i+1, j) not in visited):
                    queue.append(((i+1, j), d+1))
                    visited.add((i+1, j))
                if (j - 1 >= 0 and rooms[i][j-1] not in (0, -1) and 
                      (i, j-1) not in visited):
                    queue.append(((i, j-1), d+1))
                    visited.add((i, j-1))
                if (j + 1 < len(rooms[0]) and rooms[i][j+1] not in (0, -1) and 
                      (i, j+1) not in visited):
                    queue.append(((i, j+1), d+1))
                    visited.add((i, j+1))
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    update_dist(rooms, i, j)
