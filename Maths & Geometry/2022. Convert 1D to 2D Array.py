class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if can form valid m x n 2D array
        if m * n != len(original):
            return []

        # Init m x n 2D array with full of 0's
        res = [[0] * n for row in range(m)]

        """
        res[0][0] = original[0]
        res[0][1] = original[1]
        res[1][0] = original[2]
        res[1][1] = original[3]
        """
        for i in range(len(original)):
            row = i // n
            col = i % n
            res[row][col] = original[i]
        return res
