class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        v1, v2, v3, v4 = (A, B), (C, D), (E, F), (G, H)
        sum_of_two = (v2[0]-v1[0])*(v2[1]-v1[1]) + (v4[0]-v3[0])*(v4[1]-v3[1])
        if v1[0] > v4[0] or v1[1] > v4[1] or v3[0] > v2[0] or v3[1] > v2[1]:
            # No overlap.
            return sum_of_two
        else:
            # Overlap, sum of two minus overlap area.
            overlap = (min(v2[1], v4[1]) - max(v3[1], v1[1]))*(min(v2[0], v4[0]) - max(v3[0], v1[0]))
            return sum_of_two - overlap

