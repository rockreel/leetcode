# Recursive solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        def wild_card_match(s, p):
            if not p and not s:
                return True

            if not p:
                return False

            if not s:
                return p == '*'

            if s[0] == p[0] or p[0] == '?':
                return wild_card_match(s[1:], p[1:])
            elif p[0] == '*':
                return wild_card_match(s, p[1:]) or wild_card_match(s[1:], p)
            else:
                return False
        
        # Remove multiple *.
        p_trim = []
        for i, c in enumerate(p):
            if c != '*' or i == 0 or p[i-1] != '*':
                p_trim.append(c)
        p = ''.join(p_trim)

        return wild_card_match(s, p)

