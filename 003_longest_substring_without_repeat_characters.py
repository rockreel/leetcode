# percentage: 99.2%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_idx = {}
        max_length = 0
        curr_length = 0
        s_idx = -1
        for i, c in enumerate(s):
            if c in char_to_idx and char_to_idx[c] > s_idx:
                if curr_length > max_length:
                    max_length = curr_length
                curr_length = i - char_to_idx[c]
                s_idx = char_to_idx[c]
            else:
                curr_length += 1
            char_to_idx[c] = i
        if curr_length > max_length:
            max_length = curr_length
            
        return max_length
