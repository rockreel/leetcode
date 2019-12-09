package leetcode;
import java.lang.Math;

public class L0011ContainerWithMostWater {

  public int maxArea(int[] height) {
    int i = 0, j = height.length - 1;
    int maxArea = 0;
    while (i < j) {
      int area = Math.min(height[i], height[j]) * (j - i);
      maxArea = Math.max(area, maxArea);
      if (height[i] > height[j]) {
        j--;
      } else {
        i++;
      }
    }
    return maxArea;
  }

}
