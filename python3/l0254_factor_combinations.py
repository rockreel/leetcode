class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        # Find all factors.
        factors = []
        combinations = [[]]
        f = 2
        while n > 1:
            while n % f == 0:
                # factors.append(f)
                n //= f
                # Generate combinations here.
                new_combinations = []
                for c in combinations:
                    new_combinations.append(sorted(c + [f]))
                    prev_n = None
                    for i in range(len(c)-1, -1, -1):
                        if c[i] != prev_n:
                            new_c = c[:]
                            new_c[i] *= f
                            new_combinations.append(sorted(new_c))
                            prev_n = c[i]
                combinations = new_combinations
            f += 1

        # # Generate all combinations.
        # combinations = [[]]
        # for f in factors:
        #     new_combinations = []
        #     for c in combinations:
        #         new_combinations.append(sorted(c + [f]))
        #         prev_n = None
        #         for i in range(len(c)):
        #             if c[i] != prev_n:
        #                 new_c = c[:]
        #                 new_c[i] *= f
        #                 new_combinations.append(sorted(new_c))
        #                 prev_n = c[i]
        #     combinations = new_combinations
        # # print(combinations)

        # Dedup combinations.
        unique_combinations = []
        prev_c = None
        for c in sorted(combinations):
            if len(c) == 1:
                continue
            if c == prev_c:
                continue
            else:
                unique_combinations.append(c)
                prev_c = c

        return unique_combinations