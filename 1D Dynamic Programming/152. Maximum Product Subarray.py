class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # Max product found so far. Init = max element
        cur_max = cur_min = 1  # Keep tracks of current max and min product ending at i

        for i in nums:
            # Save cur_max before updating. cur_max = previous_max * i
            temp = cur_max * i

            # cur_max is either:
            # 1. previous max * i
            # 2. cur_min * i i.e. min negative product * i -> hence become largest
            # 3. i i.e. start a fresh number
            cur_max = max(temp, cur_min * i, i)

            # cur_min is similar: tracks most negative product that could become max later
            cur_min = min(temp, cur_min * i, i)

            # Update res after every element i
            res = max(res, cur_max)

        return res
