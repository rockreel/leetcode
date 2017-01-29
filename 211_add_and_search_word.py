class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        d = self.root
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d[''] = {}  # Mark the end of word.
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root)
        
        
    def _search(self, word, root):
        if len(word) == 0:
            return '' in root

        if word[0] != '.':
            if word[0] not in root:
                return False
            else:
                return self._search(word[1:], root[word[0]])
        else:
            for node in root.values():
                if self._search(word[1:], node):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

