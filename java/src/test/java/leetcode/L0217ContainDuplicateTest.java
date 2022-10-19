package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0217ContainDuplicateTest {

    L0217ContainDuplicate solution = new L0217ContainDuplicate();

    @Test
    public void test() {
        assertTrue(
                solution.containsDuplicate(new int[] { 1, 2, 3, 1 }));

        assertTrue(
                solution.containsDuplicate(new int[] { 1, 2, 3, 1 }));
    }

}
