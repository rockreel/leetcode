package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0020ValidParenthesesTest {

    L0020ValidParentheses solution = new L0020ValidParentheses();

    @Test
    public void test() {
        assertTrue(solution.isValid("()"));
        assertTrue(solution.isValid("()[]{}"));
        assertFalse(solution.isValid("(]"));
    }

}
