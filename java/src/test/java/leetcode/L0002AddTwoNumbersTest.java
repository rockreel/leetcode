package leetcode;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class L0002AddTwoNumbersTest {

  final L0002AddTwoNumbers solution = new L0002AddTwoNumbers();

  @Test
  public void test() {
    assertEquals(ListNode.createList(new int[] {2, 4, 6}),
        solution.addTwoNumbers(ListNode.createList(new int[] {1, 2, 3}), ListNode.createList(new int[] {1, 2, 3})));
  }

}
