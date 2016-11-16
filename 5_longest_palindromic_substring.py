# percentage: 1.26%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p_map = [[False] * len(s) for _ in range(len(s))]
        max_i = 0
        max_j = 0
        for i in range(len(s)):
            p_map[i][i] = True
            
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                p_map[i][i-1] = True
                max_i = i - 1
                max_j = i
        
        for offset in range(1, len(s)):
            for i in range(len(s) - offset):
                j = i + offset
                if p_map[i+1][j-1] and s[i] == s[j]:
                    p_map[i][j] = True
                    if max_j - max_i + 1 < j - i + 1:
                        max_i = i
                        max_j = j

        return s[max_i:max_j+1]
    
