class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # max product so far
        cur_max = cur_min = 1  # max and min product ending at i

        # For each number i
        for i in nums:
            # Save cur_max before updating
            temp = cur_max * i

            # Max is either: continue previous max, use previous min (if i negative), or reset
            cur_max = max(temp, cur_min * i, i)

            # Min tracks negative products that could become max later
            cur_min = min(temp, cur_min * i, i)

            res = max(res, cur_max)  # Update max product
        return res
