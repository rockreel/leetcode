class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for j in range(len(s), 0, -1):
            if s[:j] == s[:j][::-1]:
                return s[j:][::-1] + s
        return ''
