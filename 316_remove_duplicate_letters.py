class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        letter_count = Counter(s)
        result = ['0']
        finalized = set([])
        
        for c in s:
            letter_count[c] -= 1
            if c not in finalized:
                while c < result[-1] and letter_count[result[-1]] > 0:
                    finalized.remove(result[-1])
                    result.pop()
                result.append(c)
                finalized.add(c)

        return ''.join(result[1:])

