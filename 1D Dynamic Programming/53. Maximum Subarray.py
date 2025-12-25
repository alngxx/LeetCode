class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            # Either start a new subarray, or extend the current one
            cur = max(nums[i], cur + nums[i])
            # Update the max sum so far
            res = max(res, cur)
        return res
