from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = list(range(len(isConnected)))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 0:
                    continue
                if root[i] == root[j]:
                    continue
                for k in range(len(root)):
                    if root[k] == root[i]:
                        root[k] = root[j]
        return len(set(root))