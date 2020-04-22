class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code her
        max_len = 0
        start = -1
        char_map = dict()
            
        for i, c in enumerate(s):
            if c not in char_map and len(char_map) == 2:
                i1, c1 = sorted(
                    [(i0, c0) for c0, i0 in char_map.items()]
                )[0]
                char_map.pop(c1)
                start = i1
            char_map[c] = i
            max_len = max(max_len, i - start)
        return max_len
