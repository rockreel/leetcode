package leetcode;

public class ListNode {

   int val;
   ListNode next;

   ListNode(int x) { val = x; }

   @Override
   public boolean equals(Object o) {
      if (o == this) {
         return true;
      }

      if (!(o instanceof ListNode)) {
         return false;
      }

      ListNode p1 = this, p2 = (ListNode) o;

      while (p1 != null || p2 != null) {
         if (p1 == null) return false;
         if (p2 == null) return false;
         if (p1.val != p2.val) return false;
         p1 = p1.next;
         p2 = p2.next;
      }
      return true;
   }

   public static ListNode createList(int[] nums) {
      ListNode head = new ListNode(0);
      ListNode p = head;
      for (int i = 0; i < nums.length; i++) {
         p.next = new ListNode(nums[i]);
         p = p.next;
      }
      return head.next;
   }

}