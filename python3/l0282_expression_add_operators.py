class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def add_operators(num: str) -> List[str]:
            if len(num) == 1:
                return [num]
            results = [num] if num[0] != '0' else []
            for i in range(1, len(num)):
                for r in add_operators(num[i:]):
                    results.append(num[:i] + '+' + r)
                    results.append(num[:i] + '-' + r)
                    results.append(num[:i] + '*' + r)
                if num[0] == '0':
                    break
            return results
        
        def evaluate(exp: str) -> int:
            curr_num = ''
            op = '+'
            stack = []
            for c in exp + '+':
                if c in '+-*':
                    if op in '+-':
                        stack.append(op)
                        stack.append(int(curr_num))
                    else:
                        stack[-1] *= int(curr_num)
                    op = c
                    curr_num = ''
                else:
                    curr_num += c
            r = 0
            while stack:
                op = stack.pop(0)
                n = stack.pop(0)
                if op == '+':
                    r += n
                else:
                    r -= n
            return r
        if not num:
            return []
        result = []
        for exp in add_operators(num):
            if evaluate(exp) == target:
                result.append(exp)
        return result

