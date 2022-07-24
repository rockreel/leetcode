from common import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        serialized = []
        while queue:
            node = queue.pop(0)
            if node:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized.append('null')

        return ','.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        value = nodes.pop(0)
        if value == 'null':
            return None
        root = TreeNode(int(value))
        queue = [root]
        while nodes:
            tree_node = queue.pop(0)
            value = nodes.pop(0)
            if value == 'null':
                tree_node.left = None
            else:
                tree_node.left = TreeNode(int(value))
            value = nodes.pop(0)
            if value == 'null':
                tree_node.right = None
            else:
                tree_node.right = TreeNode(int(value))
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))