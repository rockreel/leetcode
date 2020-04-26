# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_linked_list(values):
    head = ListNode(None)
    p = head
    for v in values:
        p.next = ListNode(v)
        p = p.next
    return head.next


def convert_linked_list_to_list(llist):
    l = []
    p = llist
    while p:
        l.append(p.val)
        p = p.next
    return l


def get_linked_list_node(head, n):
    i, p = 0, head
    while i < n:
        p = p.next
        i += 1
    return p


def create_binary_tree(values):
    if not values:
        return None
    root = TreeNode(values.pop(0))
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if values:
            v = values.pop(0)
            if v is not None:
                node.left = TreeNode(v)
        if values:
            v = values.pop(0)
            if v is not None:
                node.right = TreeNode(v)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


def convert_binary_tree_to_list(tree):
    if not tree:
        return []
    queue = [tree]
    l = []
    while queue:
        node = queue.pop(0)
        if node:
            l.append(node.val)
        else:
            l.append(None)
        if node:
            queue.append(node.left)
            queue.append(node.right)

    while not l[-1]:
        l.pop()
    return l


def get_tree_node(tree, n):
    queue = [tree]
    i = 0
    while queue:
        node = queue.pop(0)
        if i == n:
            return node
        i += 1
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return None
