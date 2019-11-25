class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        class Trie(object):
            def __init__(self):
                self.root = {}
                
            def insert(self, word):
                d = self.root
                for c in word:
                    if c not in d:
                        d[c] = {}
                    d = d[c]
                d[''] = {}
            
            def search(self, word):
                d = self.root
                for c in word:
                    if c not in d:
                        return False
                    d = d[c]
                return '' in d
                
            def start_with(self, prefix):
                d = self.root
                for c in prefix:
                    if c not in d:
                        return False
                    d = d[c]
                return True
        
        def dfs(i, j, board, word, result, trie):
            # DFS start at i, j and find if word is the given word list.
            word += board[i][j]
            if not trie.start_with(word):
                return
            if trie.search(word):
                result.add(word)
                
            tmp = board[i][j]
            board[i][j] = '.'            
            if i - 1 >= 0 and board[i-1][j] != '.':
                dfs(i-1, j, board, word, result, trie)
            if i + 1 < len(board) and board[i+1][j] != '.':
                dfs(i+1, j, board, word, result, trie)
            if j - 1 >= 0 and board[i][j-1] != '.':
                dfs(i, j-1, board, word, result, trie)
            if j + 1 < len(board[0]) and board[i][j+1] != '.':
                dfs(i, j+1, board, word, result, trie)
            board[i][j] = tmp
                
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = set([])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, board, '', result, trie)
                
        return list(result)

