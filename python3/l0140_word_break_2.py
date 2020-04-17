from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dp[i]: words can be break at the end of s[:i]
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = ['']
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i].append(s[j:i])
        
        # BFS to construct all word breaks.
        word_breaks = []
        queue = [([w], len(dp)-1) for w in dp[-1]]
        while queue:
            breaks, pos = queue.pop(0)
            next_pos = pos - len(breaks[0])
            if next_pos == 0:
                word_breaks.append(breaks)
            else:
                for word in dp[pos - len(breaks[0])]:
                    queue.append(([word] + breaks, pos - len(breaks[0])))

        return [' '.join(breaks) for breaks in word_breaks]