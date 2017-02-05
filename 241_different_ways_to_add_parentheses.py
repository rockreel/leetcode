class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        try:
            return [int(input)]
        except:
            pass
        result = []
        for i, c in enumerate(input):
            if c in '+-*':
                for r1 in self.diffWaysToCompute(input[:i]):
                    for r2 in self.diffWaysToCompute(input[i+1:]):
                        if c == '+':
                            result.append(r1+r2)
                        elif c == '-':
                            result.append(r1-r2)
                        else:
                            result.append(r1*r2)
        return result

