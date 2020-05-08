class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        a = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    a.append((i, j, A[i][j]))
        b = []
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    b.append((i, j, B[i][j]))
                    
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i][1] == b[j][0]:
                    C[a[i][0]][b[j][1]] += a[i][2] * b[j][2]
        
        return C