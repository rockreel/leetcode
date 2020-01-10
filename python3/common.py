# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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