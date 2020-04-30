from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        # Stack holds last 3 numbers for calculation.
        stack = [0, '+', 0, '+', int(num[0])]
        expressions = [(num[0], stack)]  
        for i in range(1, len(num)):
            new_expressions = []
            for e, s in expressions:
                # Append number to last in stack (not adding operator) if last one is not 0.
                if s[4] != 0:
                    new_stack = s[:]
                    new_stack[4] = new_stack[4] * 10 + int(num[i])
                    new_expressions.append((e + num[i], new_stack))

                # Adding new operator and calculate stack numbers.
                if s[3] == '*':
                    # Last operation is *.
                    s[2] = s[2] * int(s[4])
                else:
                    # Last operation is + or -.
                    if s[1] == '+':
                        s[0] = s[0] + s[2]
                    else:
                        s[0] = s[0] - s[2]
                    s[1] = s[3]
                    s[2] = int(s[4])
                # Add operators.
                new_stack = s[:]
                new_stack[3] = '+'
                new_stack[4] = int(num[i])
                new_expressions.append((e + '+' + num[i], new_stack))

                new_stack = s[:]
                new_stack[3] = '-'
                new_stack[4] = int(num[i])
                new_expressions.append((e + '-' + num[i], new_stack))

                new_stack = s[:]
                new_stack[3] = '*'
                new_stack[4] = int(num[i])
                new_expressions.append((e + '*' + num[i], new_stack))

            expressions = new_expressions

        results = []
        for exp, stack in expressions:
            r = 0
            if stack[3] == '*':
                if stack[1] == '+':
                    r = stack[0] + stack[2] * stack[4]
                else:
                    r = stack[0] - stack[2] * stack[4]
            elif stack[3] == '+':
                if stack[1] == '+':
                    r = stack[0] + stack[2] + stack[4]
                else:
                    r = stack[0] - stack[2] + stack[4]
            else:
                if stack[1] == '+':
                    r = stack[0] + stack[2] - stack[4]
                else:
                    r = stack[0] - stack[2] - stack[4]
            if r == target:
                results.append(exp)
        return results


    def addOperatorsRecursive(self, num: str, target: int) -> List[str]:
        
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

