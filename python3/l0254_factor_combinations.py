from typing import List

class Solution:
    def getFactors(self, n):
      
        def factors(n, start):
            i = start
            result = []
            while i * i <= n:
                if n % i == 0:
                    for r in factors(n // i, i):
                        result.append([i] + r)
                i += 1
            result.append([n])
            return result
        
        result = factors(n, 2)
        result.pop()
        return result
