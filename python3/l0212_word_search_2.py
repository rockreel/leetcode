from typing import List

class Trie:

    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.nodes = [None] * 256

    def __init__(self):
        self._root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if node.nodes[ord(c)] is None:
                node.nodes[ord(c)] = Trie.TrieNode()
            node = node.nodes[ord(c)]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._root
        for c in word:
            if node.nodes[ord(c)] is None:
                return False
            node = node.nodes[ord(c)]
        return node.is_end

    def start_with(self, prefix: str) -> bool:
        node = self._root
        for c in prefix:
            if node.nodes[ord(c)] is None:
                return False
            node = node.nodes[ord(c)]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        queue = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                queue.append((board[i][j], [(i, j)]))
        
        result = set()
        while queue:
            word, visited = queue.pop()
            i, j = visited[-1][0], visited[-1][1]

            if not trie.start_with(word):
                continue
            
            if trie.search(word):
                result.add(word)
            
            if i - 1 >= 0 and (i-1, j) not in visited:
                queue.append((word + board[i - 1][j], visited + [(i - 1, j)]))
            if i + 1 < len(board) and (i+1, j) not in visited:
                queue.append((word + board[i + 1][j], visited + [(i + 1, j)]))
            if j - 1 >= 0 and (i, j-1) not in visited:
                queue.append((word + board[i][j - 1], visited + [(i, j - 1)]))
            if j + 1 < len(board[0]) and (i, j+1) not in visited:
                queue.append((word + board[i][j + 1], visited + [(i, j + 1)]))

        return list(result)