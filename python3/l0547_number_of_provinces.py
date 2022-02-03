from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find_root(i, root):
            if i == root[i]:
                return i
            root[i] = find_root(root[i], root)
            return root[i]

        root = list(range(len(isConnected)))
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j] == 0:
                    continue
                rooti = find_root(i, root)
                rootj = find_root(j, root)
                if rooti == rootj:
                    continue
                for k in range(len(root)):
                    if root[k] == rooti:
                        root[k] = rootj
        return len(set(root))