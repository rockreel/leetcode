class Solution:
    def reverseWords(self, s: str) -> str:
        i, j = len(s) - 1, len(s) - 1
        reversed = ''
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
                j -= 1
            while i >= 0 and s[i] != ' ':
                i -= 1
            if i != j:
                if not reversed:
                    reversed = s[i+1:j+1]
                else:
                    reversed = reversed + ' ' + s[i+1:j+1]
                j = i
        return reversed