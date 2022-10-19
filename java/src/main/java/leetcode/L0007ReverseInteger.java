package leetcode;

public class L0007ReverseInteger {

    public int reverse(int x) {
        int result = 0;
        while (x != 0) {
            int r = x % 10;
            if ((result == 214748364 && r > 7) || result > 214748364) {
                return 0;
            }
            if ((result == -214748364 && r < -8) || result < -214748364) {
                return 0;
            }
            result = result * 10 + r;
            x = x / 10;
        }
        return result;
    }

}
