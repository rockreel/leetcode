from typing import List
from collections import defaultdict

class Solution:
    def palindromePairsBrutalForce(self, words: List[str]) -> List[List[int]]:
        word_map = dict([(w, i) for i, w in enumerate(words)])
        result = set([])
        for i, word in enumerate(words):
            for j in range(len(word)+1):

                if word[:j] == word[:j][::-1]:
                    k = word_map.get(word[j:][::-1])
                    if k is not None and k != i:
                        result.add((k, i))
                if word[j:] == word[j:][::-1]:
                    k = word_map.get(word[:j][::-1])
                    if k is not None and k != i:
                        result.add((i, k))
        return [[r[0], r[1]] for r in result]

    class TrieNode:
        def __init__(self):
            self.children = {}
            # Record indices of words that match to the node. 
            # Assume i is a shorter word form palindrome, then
            # 1) shorter word at back: words[j] + words[i], use words[j] to build Trie, and search reversed words[i].
            self.indices = []
            # 2) shorter word in front: words[i] + words[j], use reversed word words[j] to build Trie, and sesarch words[i].
            self.indices_reverse = []
            
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Build a Trie.
        trie = Solution.TrieNode()
        for i, word in enumerate(words):
            current = trie
            current.indices_reverse.append(i)
            for c in word[::-1]:
                child = current.children.get(c)
                if not child:
                    current.children[c] = Solution.TrieNode()
                    child = current.children[c]
                child.indices_reverse.append(i)
                current = child
                
            current = trie
            current.indices.append(i)
            for c in word:
                child = current.children.get(c)
                if not child:
                    current.children[c] = Solution.TrieNode()
                    child = current.children[c]
                child.indices.append(i)
                current = child
        
        # Find possible candidates.
        search_map = defaultdict(list)
        for i in range(len(words)):
            current = trie
            for c in words[i]:
                if c in current.children:
                    current = current.children[c]
                else:
                    break
            else:
                search_map[i].extend(current.indices_reverse)
            
            current = trie
            for c in words[i][::-1]:
                if c in current.children:
                    current = current.children[c]
                else:
                    break
            else:
                for c in current.indices:
                    search_map[c].append(i)
        
        result = set([])
        for i in search_map:
            for j in search_map[i]:
                if i == j:
                    continue
                w = words[i] + words[j]
                if w == w[::-1]:
                    result.add((i, j))

        return [[r[0], r[1]] for r in result]