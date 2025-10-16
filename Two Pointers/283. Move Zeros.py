class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        - All elements before i are non-zero
        - All elements after i are non-zero or unprocessed
        """
        i = 0  # Point to index of next non-zero element should go to
        for j in range(len(nums)):
            # If current number is non-zero, swap it to the front with the current zero
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            # If current number is zero, keep moving j forwards and let i unchanged, so i points to 0
