class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Helper function - compute sum of digits of every integer
        def sum_of_digits(n):
            digits = [int(d) for d in str(n)]
            return sum(digits)
        
        # In-place modification
        for i in range(len(nums)):
            nums[i] = sum_of_digits(nums[i])
        
        return min(nums)