# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def _serialize(self, root, nodes):
        if root is not None:
            nodes.append(str(root.val))
            self._serialize(root.left, nodes)
            self._serialize(root.right, nodes)
        else:
            nodes.append('null')
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        self._serialize(root, nodes)
        return ','.join(nodes)
        
    def _deserialize(self, data_iter):
        node_val = next(data_iter, None)
        if node_val is None:
            return None
        
        if node_val == 'null':
            root = None
        else:
            root = TreeNode(int(node_val))
            root.left = self._deserialize(data_iter)
            root.right = self._deserialize(data_iter)
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self._deserialize(iter(data.split(',')))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

