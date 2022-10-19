package leetcode;

import java.util.Arrays;

public class L0003LongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        int[] charMap = new int[256]; // Bitmap for each char's last seen index.
        Arrays.fill(charMap, -1);
        int beginIdx = -1;
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            int charPrevIdx = charMap[(int) s.charAt(i)];
            if (charPrevIdx != -1 && beginIdx < charPrevIdx) {
                beginIdx = charPrevIdx;
            }
            charMap[(int) s.charAt(i)] = i;
            maxLength = maxLength >= (i - beginIdx) ? maxLength : (i - beginIdx);
        }
        return maxLength;
    }

}
