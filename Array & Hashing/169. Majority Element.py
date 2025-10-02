class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        1. Brute force: O(nlogn) since using sort()
        nums.sort()
        return nums[n//2]

        2. HashMap: {num : freq}
        """
        n = len(nums)
        freq = {}  # Dict to store frequency/count of element

        for num in nums:
            # If number seen in dict, increase its count by 1
            if num in freq:
                freq[num] += 1
            # If number never saw before, init its count = 1
            else:
                freq[num] = 1

        # Return the key with count > n//21
        for num in freq:
            if freq[num] > n // 2:
                return num
