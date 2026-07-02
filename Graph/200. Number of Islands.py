from ast import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ DFS: O(m * n), O(m * n)
        Similar to Flood Fill
        - Iterate through every pixel
        - Whenever found a "1", mark it as "0" and DFS its 4 neighbors. 
        - Then increment island 1 (found a new land starting point).
        """
        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            # if current pixel out of bounds or not "land", return
            if (r < 0) or (c < 0) or (r > rows - 1) or (c > cols - 1) or grid[r][c] != "1":
                return
            
            # otherwise, mark this as visited ("0") and DFS all 4 neighbors
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1
        return island