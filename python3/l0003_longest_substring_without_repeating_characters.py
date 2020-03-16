class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        max_start_idx = -1
        for i, c in enumerate(s):
            if c in char_map:
                max_start_idx = max(char_map[c], max_start_idx)
            char_map[c] = i   
            max_len = max(max_len, i - max_start_idx)
        return max_len