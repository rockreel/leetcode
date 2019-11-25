class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValidTwoDigit(s):
            # Must be in 10 - 26.
            if s[0] not in '12':
                return False
            if s[0] == '2' and s[1] not in '0123456':
                return False
            return True
        
        def isValidOneDigit(s):
            # Must be in 1 - 9.
            return s != '0'
        
        if not s:
            return 0
        
        # Num of ways to decode s[:i].
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        if isValidOneDigit(s[0]):
            dp[1] = 1
        
        for i in range(2, len(dp)):
            if isValidOneDigit(s[i-1]):
                dp[i] += dp[i-1]
            if isValidTwoDigit(s[i-2:i]):
                dp[i] += dp[i-2]

        return dp[-1]

