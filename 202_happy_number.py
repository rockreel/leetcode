class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            else:
                visited.add(n)
            sq_sum = 0
            while n > 0:
                sq_sum += (n % 10) ** 2
                n = n / 10
            n = sq_sum
        return False

