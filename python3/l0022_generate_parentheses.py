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