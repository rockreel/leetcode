class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = { 'root': {} }
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self._trie['root']
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[''] = None  

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self._trie['root']
        return self._search(word, node)

    def _search(self, word, node):
        if not word:
            return '' in node

        c = word[0]
        if c != '.':
            if c not in node:
                return False
            else:
                return self._search(word[1:], node[c])
        else:
            for k in node:
                if k == '':
                    continue
                if self._search(word[1:], node[k]):
                    return True    
            return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)