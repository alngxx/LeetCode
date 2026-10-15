class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """ Sorting + Two Pointers: O(n log n), O(1) """
        nums.sort()
        count = 0 
        i, j = 0, len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]
            if total < k:
                i += 1
            elif total > k:
                j -= 1
            else:
                i += 1
                j -= 1
                count += 1
        
        return count