# percentage: 84.3%
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        head = ListNode(None)
        p = head
        head_nodes = [(l.val, l) for l in lists if l]
        heapq.heapify(head_nodes)
        while head_nodes:
            _, n = heapq.heappop(head_nodes)
            if n.next:
                heapq.heappush(head_nodes, (n.next.val, n.next))
            p.next = n
            p = p.next
        return head.next
