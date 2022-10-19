package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0009PalindromeNumberTest {

    L0009PalindromeNumber solution = new L0009PalindromeNumber();

    @Test
    public void test() {
        assertTrue(solution.isPalindrome(121));
        assertFalse(solution.isPalindrome(-121));
        assertFalse(solution.isPalindrome(10));
    }

}
