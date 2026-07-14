class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """ Sliding Window: O(n), O(1)
        1. Expand right, cur_sum += nums[r]
        2. When window size == k, update max_sum, then shrink left
        3. Return max_sum / k
        """
        l = cur_sum = 0
        max_sum = float('-inf')

        for r in range(len(nums)):
            cur_sum += nums[r]

            if (r - l + 1) == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[l]
                l += 1
        
        return max_sum / k