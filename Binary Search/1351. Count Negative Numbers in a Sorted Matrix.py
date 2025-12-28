class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)  # row
        n = len(grid[0])  # column

        for row in grid:
            # Binary search to find first negative number in each row
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                # If current number is negative,
                # first negative could be at mid or to the left of mid
                if row[mid] < 0:
                    right = mid
                # Else, first negative must be to the right of mid
                else:
                    left = mid + 1
            # At this point, left is index of first negative number
            count += n - left

        return count
