package leetcode;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class L0003LongestSubstringWithoutRepeatingCharactersTest {

  final L0003LongestSubstringWithoutRepeatingCharacters solution = new L0003LongestSubstringWithoutRepeatingCharacters();

  @Test
  public void test() {
    assertEquals(3, solution.lengthOfLongestSubstring("abcabcbb"));
    assertEquals(1, solution.lengthOfLongestSubstring("bbbbb"));
    assertEquals(3, solution.lengthOfLongestSubstring("pwwkew"));
  }

}
