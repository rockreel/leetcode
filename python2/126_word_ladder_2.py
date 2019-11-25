class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def find_neighbors(word, word_set):
            neighbors = []
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    neighbor = word[:i]+c+word[i+1:]
                    if neighbor in word_set:
                        neighbors.append(neighbor)
            return neighbors
                    
        # BFS to find shortest path.
        wordlist.add(endWord)
        wordlist.remove(beginWord)
        from collections import deque
        queue = deque()
        queue.append((beginWord, [], 0))
        paths = []
        current_level = 0
        max_level = None
        visited = set()
        neighbor_map = {}
        while queue:
            word, path, level = queue.popleft()

            if word == endWord:
                max_level = level
                paths.append(path + [word])
                continue
                
            if level == max_level:
                continue
                
            if level > current_level:
                current_level = level
                wordlist.difference_update(visited)
                visited = set()
                neighbor_map = {}
            
            # Cache neighbor calculation.
            if word in neighbor_map:
                neighbors = neighbor_map[word]
            else:
                neighbors = find_neighbors(word, wordlist)
                neighbor_map[word] = neighbors
                
            for neighbor in neighbors:
                queue.append((neighbor, path + [word], level+1))
                visited.add(neighbor)
                
        return paths

