class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)

        # Edge case: 1x1 matrix
        if n == 1:
            return mat[0][0]

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - i - 1]

        # Handle duplicate of middle element in odd matrix
        if n % 2 == 1:
            mid = n // 2
            return total - mat[mid][mid]

        return total
