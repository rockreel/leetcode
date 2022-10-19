package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0007ReverseIntegerTest {

    final L0007ReverseInteger solution = new L0007ReverseInteger();

    @Test
    public void test() {
        assertEquals(321, solution.reverse(123));
        assertEquals(-321, solution.reverse(-123));
        assertEquals(21, solution.reverse(120));
        assertEquals(0, solution.reverse(1534236469));
        assertEquals(0, solution.reverse(-2147483648));
    }

}
