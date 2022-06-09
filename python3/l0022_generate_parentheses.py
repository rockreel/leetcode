from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generateParen(open_left, close_left):
            if open_left == 0 and close_left == 1:
                return [')']
            result = []
            if open_left > 0:
                for r in generateParen(open_left - 1, close_left):
                    result.append('(' + r)
            
            if close_left > open_left:
                for r in generateParen(open_left, close_left - 1):
                    result.append(')' + r)
            return result
        
        return generateParen(n, n)

    def generateParenthesisIterative(self, n: int) -> List[str]:
        queue = [('', 0, 0)]
        result = []
        while queue:
            s, n_open, n_close = queue.pop(0)
            if n_open == n and n_close == n:
                result.append(s)
                continue
            if n_open > n_close:
                queue.append((s + ')', n_open, n_close + 1))
            if n_open < n:
                queue.append((s + '(', n_open + 1, n_close))
        
        return result