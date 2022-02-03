from typing import List
from collections import defaultdict

class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find_root(i, root):
            # Compression find.
            if i == root[i]:
                return i
            root[i] = find_root(root[i], root)
            return root[i]
    
        root = list(range(len(s)))
        for p in pairs:
            root0 = find_root(p[0], root)
            root1 = find_root(p[1], root)
            if root0 != root1:
                root[root0] = root1
        
        root_to_letters = defaultdict(list)
        for i in range(len(root)):
            root_to_letters[find_root(i, root)].append(s[i])
        for k in root_to_letters:
            root_to_letters[k] = sorted(root_to_letters[k])
        letters = []
        for i in range(len(s)):
            letters.append(root_to_letters[find_root(i, root)].pop(0))
        
        return ''.join(letters)

    def smallestStringWithSwapsGraphTraverse(self, s: str, pairs: List[List[int]]) -> str:
        smallest = s
        queue = [s]
        visited = set([])
        while queue:
            ss = queue.pop(0)
            visited.add(ss)
            smallest = min(ss, smallest)
            for p in pairs:
                s_list = list(ss)
                s_list[p[0]], s_list[p[1]] = s_list[p[1]], s_list[p[0]]
                s_swapped = ''.join(s_list)
                if s_swapped not in visited:
                    queue.append(s_swapped)
        return smallest