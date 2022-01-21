class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for i, c in enumerate(s):
            if c not in char_dict:
                char_dict[c] = (1, i)
            else:
                char_dict[c] = (char_dict[c][0] + 1, i)
        index = len(s)
        for c, v in char_dict.items():
            if v[0] == 1:
                index = min(index, v[1])
        return index if index < len(s) else -1