class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if not s and not t:
            return False
        
        if not s:
            return len(t) == 1
        
        if not t:
            return len(s) == 1
        
        if s[0] == t[0]:
            if self.isOneEditDistance(s[1:], t[1:]):
                return True

        if s[0] != t[0]:
            if s[1:] == t or s == t[1:] or s[1:] == t[1:]:
                return True
        
        return False