class MapSum:

    class Node:
        def __init__(self):
            self._value = 0
            self._children = {}
            
        def add_child(self, char, node):
            self._children[char] = node
            
        def get_child(self, char):
            return self._children.get(char)
        
        def get_all_children(self):
            return self._children.values()
        
        def set_value(self, value):
            self._value = value
        
        def get_value(self):
            return self._value

    def __init__(self):
        self._root = MapSum.Node()

    def insert(self, key: str, val: int) -> None:
        curr = self._root
        for c in key:
            child = curr.get_child(c)
            if not child:
                child = MapSum.Node()
                curr.add_child(c, child)
            curr = child
        curr.set_value(val)

    def sum(self, prefix: str) -> int:
        curr = self._root
        for c in prefix:
            child = curr.get_child(c)
            if not child:
                return 0
            curr = child
        return self._cal_sum(curr)
        
    def _cal_sum(self, node) -> int:
        if not node:
            return 0
        result = node.get_value()
        for c in node.get_all_children():
            result += self._cal_sum(c)
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)