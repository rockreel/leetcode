class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
            
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
                # Match, either keep using * pattern or skip * pattern.
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                # Not match skip the * pattern.
                return self.isMatch(s, p[2:])
        else:
            if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False

