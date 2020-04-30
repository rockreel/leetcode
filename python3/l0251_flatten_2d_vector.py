class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self._vec2d = vec2d
        self._row = len(self._vec2d)
        self._col = -1
        for i in range(len(self._vec2d)):
            for j in range(len(self._vec2d[i])):
                self._row = i
                self._col = j
                break
            if self._col != -1:
                break  

    # @return {int} a next element
    def next(self):
        # Write your code here
        val = self._vec2d[self._row][self._col]
        self._col += 1
        while self._row < len(self._vec2d) and not self.hasNext():
            self._row += 1
            self._col = 0
        return val
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return self._row < len(self._vec2d) and self._col < len(self._vec2d[self._row])
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())