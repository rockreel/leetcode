class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def genParen(num_open_left, num_close_left):
            if num_open_left == 0 and num_close_left == 1:
                return [')']
            result = []
            if num_open_left > 0:
                for r in genParen(num_open_left-1, num_close_left):
                    result.append('('+r)
            if num_close_left > num_open_left:
                for r in genParen(num_open_left, num_close_left-1):
                    result.append(')'+r)
            return result
            
        return genParen(n, n)

