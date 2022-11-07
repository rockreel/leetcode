package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0242ValidAnagramTest {

  L0242ValidAnagram solution = new L0242ValidAnagram();

  @Test
  public void test() {
    assertTrue(
        solution.isAnagram("anagram", "nagaram"));

    assertFalse(
        solution.isAnagram("rat", "car"));
  }

}
