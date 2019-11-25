class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def add_operator(num, target, result, prev_num, expression, expressions):
            if not num and result == target:
                expressions.append(expression)
                return

            for i in range(1, len(num)+1):
                # Exclude case have number like 0xxx. 
                if i > 1 and num[0] == '0':
                    return
                
                curr_num = int(num[:i])
                if expression:
                    # Operator +.
                    add_operator(
                        num[i:], target, result+curr_num, curr_num,
                        expression+'+'+num[:i], expressions)
                    # Operator -.
                    add_operator(
                        num[i:], target, result-curr_num, -curr_num,
                        expression+'-'+num[:i], expressions)
                    # Operator *. The prev number is the whole block of a*b*c....
                    # And to calulate result, it first need to substract prev number
                    # from result, then add prev number multiply curr number. 
                    add_operator(
                        num[i:], target, result-prev_num+prev_num*curr_num,
                        prev_num*curr_num, expression+'*'+num[:i], expressions)
                else:
                    add_operator(
                        num[i:], target, curr_num, curr_num, num[:i], expressions)

        expressions = []
        add_operator(num, target, 0, 0, '', expressions)
        return expressions

