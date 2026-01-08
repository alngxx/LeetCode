class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        # Two pointers
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # Update closet sum
                if abs(total - target) < abs(res - target):
                    res = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total  # early return if total == target
        return res
