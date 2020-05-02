"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
class Celebrity:

    knows_graph = set()

    def knows(a, b):
        return (a, b) in Celebrity.knows_graph

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        celebrities = set(range(n))
        while len(celebrities) > 1:
            p1 = celebrities.pop()
            p2 = celebrities.pop()
            if Celebrity.knows(p1, p2):
                celebrities.add(p2)
            else:
                celebrities.add(p1)
        p = celebrities.pop()
        for i in range(n):
            if i != p:
                if Celebrity.knows(p, i):
                    return -1
                elif not Celebrity.knows(i, p):
                    return -1
        return p