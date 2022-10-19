package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0002AddTwoNumbersTest {

    final L0002AddTwoNumbers solution = new L0002AddTwoNumbers();

    @Test
    public void test() {
        assertEquals(ListNode.createList(new int[] { 7, 0, 8 }),
                solution.addTwoNumbers(ListNode.createList(new int[] { 2, 4, 3 }),
                        ListNode.createList(new int[] { 5, 6, 4 })));
    }

}
