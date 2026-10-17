class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        """ Hashmap of rows: O(n²), O(n²)
        1. Count each row as a tuple in a hashmap
        2. Build each column by reading grid[i][j] down the rows, as a tuple
        3. Add the number of rows equal to that column
        """
        n = len(grid)

        row_count = {}
        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1
        
        # build list of columns
        cols = []
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            cols.append(col)
        
        res = 0
        for col in cols:
            key = tuple(col)
            res += row_count.get(key, 0)
        
        return res