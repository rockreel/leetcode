class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map_1 = dict()
        char_map_2 = dict()
        for c1, c2 in zip(s, t):
            if c1 not in char_map_1 and c2 not in char_map_2:
                char_map_1[c1] = c2
                char_map_2[c2] = c1
            elif c1 in char_map_1 and c2 in char_map_2:
                if char_map_1[c1] != c2 or char_map_2[c2] != c1:
                    return False
            else:
                return False
        return True