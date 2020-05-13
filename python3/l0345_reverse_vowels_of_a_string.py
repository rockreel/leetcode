class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i].lower() not in 'aeiou':
                i += 1
            while i < j and s[j].lower() not in 'aeiou':
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
