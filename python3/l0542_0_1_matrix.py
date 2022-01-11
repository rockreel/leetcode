from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_dist = len(mat)+len(mat[0])
        dist = [[max_dist] * len(mat[0]) for _ in mat]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if i + 1 < len(mat):
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                    if j - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
                    if j + 1 < len(mat[0]):
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if i + 1 < len(mat):
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                    if j - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
                    if j + 1 < len(mat[0]):
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

        return dist

    def updateMatrixBFS(self, mat: List[List[int]]) -> List[List[int]]:
        max_dist = len(mat)+len(mat[0])
        dist = [[max_dist] * len(mat[0]) for _ in mat]
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, d = queue.pop()

            if d < dist[i][j]:
                dist[i][j] = d
            if i - 1 >= 0 and d + 1 < dist[i-1][j]:
                queue.append((i-1, j, d+1))

            if i + 1 < len(mat) and d + 1 < dist[i+1][j]:
                queue.append((i+1, j, d+1))

            if j - 1 >= 0 and d + 1 < dist[i][j-1]:
                queue.append((i, j-1, d+1))

            if j + 1 < len(mat[0]) and d + 1 < dist[i][j+1]:
                queue.append((i, j+1, d+1))

        return dist