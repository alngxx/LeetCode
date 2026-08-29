class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """ Kadane's Algorithm: O(n), O(1)
        This is a variant of LeetCode 53 - Maximum Subarray, there're 2 cases
        1. Non-circular
        - max_sum is in the middle
        - This is normal Kadane's Algorithm
        2. Circular
        - prefix...middle...suffix
        - max_sum = prefix + suffix = total - middle
        - Thus, we use Kadane to find min(middle) to maximize max_sum
        """
        total = sum(nums)
        min_sum = cur_min = nums[0]
        max_sum = cur_max = nums[0]

        for num in nums[1:]:
            # case 1: max_sum is in middle
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)

            # case 2: max_sum = total - min_sum
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
        
        # edge case: if all nums < 0, min_sum == total
        # thus return 0, not max_sum
        # e.g. [-3,-2,-3] return 0, not -2
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum