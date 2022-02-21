from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False
            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Solution.TrieNode()
        for word in dictionary:
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Solution.TrieNode()
                curr = curr.children[c]
            curr.is_word = True
            
        result = []
        for word in sentence.split(' '):
            curr = trie
            for i, c in enumerate(word):
                if curr.is_word:
                    result.append(word[:i])
                    break
                if c not in curr.children:
                    result.append(word)
                    break
                curr = curr.children[c]
            else:
                result.append(word)

        return ' '.join(result)