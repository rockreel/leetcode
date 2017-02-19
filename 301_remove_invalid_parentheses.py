class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        queue = [s]
        visited = set([s])
        result = []
        while queue:
            s0 = queue.pop(0)
            if result and len(s0) < len(result[0]):
                # Only need to find string with maximum length.
                break
            if is_valid(s0):
                result.append(s0)
            else:
                for i in range(len(s0)):
                    if s0[i] not in ('(', ')'):
                        continue
                    s1 = s0[:i]+s0[i+1:]
                    if s1 not in visited:
                        visited.add(s1)
                        queue.append(s1)
        return result

