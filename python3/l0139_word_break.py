from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]: if s[:i] can break by dict.
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i-1, -1, -1):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreakRecursive(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        for word in wordDict:
            if s[:len(word)] == word and self.wordBreak(s[len(word):], wordDict):
                return True
        return False