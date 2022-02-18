from functools import lru_cache

class Solution:
    def numTilings(self, n: int) -> int:
        
        @lru_cache(None)
        def num_tilings(n, mode):
            result = 0
            if n == 0:
                result = 1
            elif n == 1:
                if mode == 0:
                    result = 1
                else:
                    result = 0
            elif n == 2:
                if mode == 0:
                    result = 2
                else:
                    result = 1
            else:
                if mode == 0:
                    result = num_tilings(n-1, 1) + num_tilings(n-1, 2) + num_tilings(n-1, 0) + num_tilings(n-2, 0)
                elif mode == 1:
                    result = num_tilings(n-2, 0) + num_tilings(n-1, 2)
                else:
                    result = num_tilings(n-2, 0) + num_tilings(n-1, 1)
            return result
        
        return num_tilings(n, 0) % (10**9 + 7)
        