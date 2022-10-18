package leetcode;

import java.util.List;
import java.util.stream.Collectors;

import com.google.common.collect.Lists;
import org.junit.Test;

import static org.junit.Assert.*;

public class L00153SumTest {

  L00153Sum solution = new L00153Sum();

  @Test
  public void test() {
    assertEquals(
        Lists.newArrayList(
          Lists.newArrayList(-1, -1, 2),
          Lists.newArrayList(-1, 0, 1)),
        sort(solution.threeSum(new int[] {-1, 0, 1, 2, -1, -4}))
    );
  }

  public List<List<Integer>> sort(List<List<Integer>> r) {
    return r.stream().sorted((r1, r2) -> {
      for (int i = 0; i < Math.min(r1.size(), r2.size()); i++) {
        int c = r1.get(i).compareTo(r2.get(i));
        if (c != 0) {
          return c;
        }
      }
      return Integer.compare(r1.size(), r2.size());
    }).collect(Collectors.toList());
  }

}
