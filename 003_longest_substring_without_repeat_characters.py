class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_to_idx = {}
        max_len = 0
        start = 0  # Current non-repeating substring start position.
        for i, c in enumerate(s):
            if c in c_to_idx and c_to_idx[c] >= start:
                start = c_to_idx[c] + 1
            c_to_idx[c] = i
            max_len = max(max_len, i - start + 1)
        return max_len