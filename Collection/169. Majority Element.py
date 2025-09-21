class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        1. Brute force: O(nlogn) since using sort()
        nums.sort()
        return nums[n//2]

        2. HashMap: {number : frequency}
        """
        n = len(nums)
        count = {}  # Dict to store frequency/count of element

        for num in nums:
            # If number seen in dict, increase its count by 1
            if num in count:
                count[num] += 1
            # If number never saw before, init its count = 1
            else:
                count[num] = 1

        # Return the key with count > n//2
        for key in count:
            if count[key] > n // 2:
                return key
