class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        '''
        Intuition
        Keep track of the smallest number seen so far while moving through the array.
        At each step, we check if current number (nums[i]) >= min and nums[i] - min largest
        If not, we update the min = nums[i]
        '''

        # Default result
        res = -1

        # Min always equal smallest number
        min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > min:
                res = max(res, nums[i] - min)
            else:
                min = nums[i]

        return res
