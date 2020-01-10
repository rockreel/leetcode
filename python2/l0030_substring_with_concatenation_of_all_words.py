class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def findall(s, substr):
            result = []
            begin = 0
            while begin < len(s):
                idx = s.find(substr, begin)
                if idx == -1:
                    break
                result.append(idx)
                begin = idx + 1
            return result
        
        if not words:
            return []
        len_word = len(words[0])
        if len(s) < len(words) * len_word:
            return []
        
        # Build mapping based on string search.
        from collections import defaultdict
        index_to_word = {}
        word_to_count = defaultdict(int)
        for w in words:
            if w not in word_to_count:
                for idx in findall(s, w):
                    index_to_word[idx] = w
            word_to_count[w] += 1

        # Search through string to find all concantenation.
        result = []
        for idx in index_to_word.keys():
            visited_word_to_count = defaultdict(int)
            for i in range(idx, idx+len_word*len(words), len_word):
                if i in index_to_word:
                    visited_word_to_count[index_to_word[i]] += 1
                    if  visited_word_to_count[index_to_word[i]] > word_to_count[index_to_word[i]]:
                        break
                else:
                    break
            else:
                result.append(idx)
            
        return result
