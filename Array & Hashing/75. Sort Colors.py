class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        Counting Sort: count each color, then overwrite the original array
        Time complexity: O(n)
        Space complexity: O(1) 
        """
        count = [0] * 3      # List of three store count of 0's, 1's, 2's
        for num in nums:
            count[num] += 1
        
        # Fill first count[0] with 0's
        # Fill next count[1] with 1's
        # Fill last count[2] with 2's
        for i in range(count[0]):
            nums[i] = 0
        for j in range(count[0], len(nums) - count[2]):
            nums[j] = 1
        for k in range(count[0] + count[1], len(nums)):
            nums[k] = 2