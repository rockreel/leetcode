from typing import List
from typing import Tuple
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        permutation = []
        k = k - 1
        while nums:
            size_of_each_number_section = math.factorial(len(nums)-1)
            permutation.append(nums.pop(k // size_of_each_number_section))
            k = k % size_of_each_number_section
        return ''.join(permutation)