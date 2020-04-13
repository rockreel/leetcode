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


def create_binary_tree(values):
    if not values:
        return None
    root = TreeNode(values.pop(0))
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if values:
            node.left = TreeNode(values.pop(0))
        if values:
            node.right = TreeNode(values.pop(0))
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