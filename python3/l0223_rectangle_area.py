class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        v11 = (A, B)
        v12 = (C, D)
        v21 = (E, F)
        v22 = (G, H)
        area = (
            (v12[0] - v11[0]) * (v12[1] - v11[1]) +
            (v22[0] - v21[0]) * (v22[1] - v21[1])
        )
        
        if (v11[0] > v22[0] or v11[1] > v22[1] or
            v12[0] < v21[0] or v12[1] < v21[1]):
            return area
        else:
            v31 = (max(v11[0], v21[0]), max(v11[1], v21[1]))
            v32 = (min(v12[0], v22[0]), min(v12[1], v22[1]))
            overlap = (v32[0] - v31[0]) * (v32[1] - v31[1])
            return area - overlap
