import bisect

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        combinations = [[]]
        f = 2
        while n > 1:
            while n % f == 0:
                n //= f
                # Generate combinations here.
                new_combinations = []
                for c in combinations:
                    new_c = sorted(c + [f])
                    # Maintain a sorted order of combinarions and only insert if it is not there.
                    j = bisect.bisect_left(new_combinations, new_c)
                    if j >= len(new_combinations) or new_combinations[j] != new_c:
                        new_combinations.insert(j, new_c)
                    prev_n = None
                    for i in range(len(c)):
                        if c[i] != prev_n:
                            prev_n = c[i]
                            new_c = c[:]
                            new_c[i] *= f
                            new_c = sorted(new_c)
                            # Maintain a sorted order of combinarions and only insert if it is not there.
                            j = bisect.bisect_left(new_combinations, new_c)
                            if j >= len(new_combinations) or new_combinations[j] != new_c:
                                new_combinations.insert(j, new_c)
    
                combinations = new_combinations
            f += 1

        combinations.pop()  # Remove the one which is the number itself.
        return combinations