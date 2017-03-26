class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_idx = {}
        curr_len = 0
        max_len = 0
        s_idx = -1
        for i, c in enumerate(s):
            if c in char_to_idx and char_to_idx[c] > s_idx:
                curr_len = i - char_to_idx[c]
                s_idx = char_to_idx[c]
            else:
                curr_len += 1
            max_len = max(curr_len, max_len)
            char_to_idx[c] = i
        return max(curr_len, max_len)

