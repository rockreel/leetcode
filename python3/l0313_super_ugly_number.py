class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        nums = [1]
        indices = [0] * len(primes)
        while len(nums) < n:
            idx = 0
            min_ = primes[idx] * nums[indices[idx]]
            for i, p in enumerate(primes):
                if p * nums[indices[i]] < min_:
                    idx = i
                    min_ = p * nums[indices[i]]
            if min_ != nums[-1]:
                nums.append(min_)
            indices[idx] += 1
        
        return nums[-1]
