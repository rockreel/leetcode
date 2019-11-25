class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Which words can be put at with last letter being at i-1.
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = ['']
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i-len(word)] and word == s[i-len(word):i]:
                    dp[i].append(word)
    
        # BFS through dp[] to construct all breaks.
        wordbreaks = []
        queue = [(w, len(dp)-1-len(w)) for w in dp[-1]] # Wordbreak so far and next dp position.
            
        while queue:
            wordbreak, idx = queue.pop(0)
            if idx == 0:
                wordbreaks.append(wordbreak)
                continue
            for word in dp[idx]:
                queue.append((word+' '+wordbreak, idx-len(word)))

        return wordbreaks

