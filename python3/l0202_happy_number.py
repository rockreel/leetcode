class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set([n])
        while True:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            if s == 1:
                return True
            elif s in num_set:
                return False
            n = s
            num_set.add(n)
