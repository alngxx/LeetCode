class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """ Prefix Sum: O(n), O(1)
        Continously compare running leftSum and rightSum
        """
        left = 0
        total = sum(nums)

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
            
        return -1