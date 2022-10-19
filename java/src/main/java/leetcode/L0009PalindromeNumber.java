package leetcode;

public class L0009PalindromeNumber {

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int r = 0;
        int x0 = x;
        while (x0 > 0) {
            r = r * 10 + x0 % 10;
            x0 = x0 / 10;
        }
        return r == x;
    }

}
