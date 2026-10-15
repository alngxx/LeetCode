class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """ Sliding Window: O(n), O(1) 
        This is variable window-size problem - similar to LC1004
        """
        l = 0
        res = 0
        delete = 1

        for r in range(len(nums)):
            # 1. slide right: use delete if encounter 0
            if nums[r] == 0:
                delete -= 1
            
            # 2. check condition: if run out of delete
            while delete < 0:
                # 3. shrink left: if nums[l] is 0, restore delete
                if nums[l] == 0:
                    delete += 1
                l += 1
            
            # 4. update res: not r - l + 1 since not include that one 0
            res = max(res, r - l)
        return res