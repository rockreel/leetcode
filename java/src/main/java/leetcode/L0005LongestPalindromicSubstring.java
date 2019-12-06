package leetcode;

public class L0005LongestPalindromicSubstring {

  public String longestPalindrome(String s) {
    String maxSub = "";
    // dp[i][j]: if s.substring(i, j) is palindrome.
    boolean[][] dp = new boolean[s.length()+1][s.length()+1];
    for (int offset = 0; offset < s.length() + 1; offset++) {
      for (int i = 0; i < s.length() + 1 - offset; i++) {
        int j = i + offset;
        if (offset == 0 || offset == 1) {
          dp[i][j] = true;
        } else if (s.charAt(i) == s.charAt(j-1) && dp[i+1][j-1]) {
          dp[i][j] = true;
        }
        if (dp[i][j] && offset > maxSub.length()) {
          maxSub = s.substring(i, i+offset);
        }
      }
    }
    return maxSub;
  }

}
