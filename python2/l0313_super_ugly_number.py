class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import sys
        # Index of generated ugly number for each prime to mulitple
        # to generate next ugly number candidate.
        indices = [0] * len(primes)
        ugly_nums = [1]
        while len(ugly_nums) < n:
            next_ugly = sys.maxint
            next_indices = []
            for i in range(len(primes)):
                if ugly_nums[indices[i]] * primes[i] < next_ugly :
                    next_ugly = ugly_nums[indices[i]] * primes[i]
                    next_indices = [i]
                elif ugly_nums[indices[i]] * primes[i] == next_ugly:
                    next_indices.append(i)
            ugly_nums.append(next_ugly)
            for i in next_indices:
                indices[i] += 1
                
        return ugly_nums[-1]

