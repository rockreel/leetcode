from common import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        results = []
        for i, c in enumerate(input):
            if c not in '+-*':
                continue
            for r1 in self.diffWaysToCompute(input[:i]):
                for r2 in self.diffWaysToCompute(input[i+1:]):
                    if c == '+':
                        r = r1 + r2
                    elif c == '-':
                        r = r1 - r2
                    else:
                        r = r1 * r2
                    results.append(r)
        return results
