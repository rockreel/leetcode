package leetcode;

public class L0002AddTwoNumbers {

  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode head = new ListNode(0);
    ListNode p1 = l1, p2 = l2, p0 = head;
    int carry = 0;
    while (carry != 0 || p1 != null || p2 != null) {
      int v1 = p1 != null ? p1.val : 0;
      int v2 = p2 != null ? p2.val : 0;

      // Calculate node value.
      int v0 = v1 + v2 + carry;
      carry = v0 / 10;
      v0 = v0 % 10;
      p0.next = new ListNode(v0);

      // Move to next node.
      p0 = p0.next;
      if (p1 != null) p1 = p1.next;
      if (p2 != null) p2 = p2.next;
    }

    return head.next;
  }

}
