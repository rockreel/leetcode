package leetcode;

import java.util.Arrays;

import org.junit.Test;

import static junit.framework.TestCase.assertTrue;

public class L0005LongestPalindromicSubstringTest {

  final L0005LongestPalindromicSubstring solution = new L0005LongestPalindromicSubstring();

  @Test
  public void test() {
    assertTrue(Arrays.asList("bab", "aba").contains(solution.longestPalindrome("babad")));
    assertTrue(Arrays.asList("bb").contains(solution.longestPalindrome("cbbd")));
  }

}
