class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force: Using two for loops
        for i in range(len(nums))
            for j in range(i+1, len(nums))
        Since may not use same element twice, j iterates from i+1
        --> O(n^2)
        '''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        HashMap - Dict in Python
        Instead of checking all pairs (two loops takes O(n²)),
        we can use a hash map (dictionary in Python)
        to store numbers already seen and their indices.

        If complement seen in Dict, return their indices
        Input:
        nums = [2, 7, 11, 15], target = 9
        i=0 → nums[0] = 2, complement = 7 → not in seen, store {2:0}
        i=1 → nums[1] = 7, complement = 2 → ✅ found in seen → return [0,1]
        -> O(n)
        '''
        # Dictionary to store seen index (i) of nums[i]
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                # If complement found, return its index and nums[i] index
                return [seen[complement], i]

            # Store current number as a key in dict seen
            seen[nums[i]] = i
