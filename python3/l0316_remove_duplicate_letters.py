from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_count = Counter(s)
        visited = set()
        result = ['0']
        
        for c in s:
            letter_count[c] -= 1
            if c not in visited:
                while c < result[-1] and letter_count[result[-1]] > 0:
                    visited.remove(result[-1])
                    result.pop()
                result.append(c)
                visited.add(c)
        
        return ''.join(result[1:])
