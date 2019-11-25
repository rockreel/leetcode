class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s2t_map = {}
        t2s_map = {}
        for s0, t0 in zip(s, t):
            if s0 not in s2t_map and t0 not in t2s_map:
                s2t_map[s0] = t0
                t2s_map[t0] = s0
            elif s0 not in s2t_map or t0 not in t2s_map:
                return False
            elif s2t_map[s0] != t0 or t2s_map[t0] != s0:
                return False
        return True
