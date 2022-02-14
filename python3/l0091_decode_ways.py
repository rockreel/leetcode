from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        def is_valid_code(s):
            if len(s) > 2:
                return False
            if s[0] == '0':
                return False
            if len(s) == 2 and s[0] > '2':
                return False
            if len(s) == 2 and s[0] == '2' and s[1] > '6':
                return False
            return True
        
        @lru_cache
        def num_decoding(s):
            if not s:
                return 1
            result = 0
            if is_valid_code(s[0]):
                result += num_decoding(s[1:])
            if len(s) >= 2 and is_valid_code(s[:2]):
                result += num_decoding(s[2:])
            return result
        return num_decoding(s)