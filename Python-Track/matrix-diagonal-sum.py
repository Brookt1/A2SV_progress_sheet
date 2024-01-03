class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dia_sum=0
        n=len(mat)
        for i in range(n):
            dia_sum+=mat[i][i]
        for i in range(n):
            if i!=n-i-1:
                dia_sum+=mat[i][n-i-1]
        return dia_sum

        