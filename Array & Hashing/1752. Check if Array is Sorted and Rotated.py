class Solution:
    def check(self, nums: List[int]) -> bool:
        """ The sorted array must only 
        1. Have 1 break and tail < head (rotated)
        2. or 0 break but tail ? head (no rotated)
        """
        n = len(nums)
        if n <= 1:
            return True

        break_count = 0    # Count the number of break in the entire array
        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                break_count += 1
            if break_count > 1:     # break_count >= 2 means array is not sorted
                return False
        
        # Check if the array is sorted but rotated: [3, 4, 5, 1, 2] has 1 break and 2 < 3
        if break_count == 1 and nums[-1] > nums[0]:
            return False

        return True        