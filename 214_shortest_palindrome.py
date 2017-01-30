class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = s + '#' + s[::-1]
        # Max length of equal prefix/suffix for p[:i+1].
        # See KMP algorithm for the idea.
        n = [0] * len(p)

        for i in range(1, len(p)):
            next = n[i-1]
            while next > 0 and p[next] != p[i]:
                next = n[next-1]
            n[i] = next + 1

        return s[n[-1]:][::-1] + s

